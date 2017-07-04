import sys
import pika

from obnl.impl.message import MetaMessage, AttributeMessage, SimulatorConnection, NextStep, SchedulerConnection, Quit


class Node(object):
    """
    This is the base class for all Nodes of the system
    """

    SCHEDULER_NAME = 'scheduler'

    LOCAL_NODE_QUEUE = 'obnl.local.node.'
    """Base of every local queue (followed by the name of the Node)"""
    LOCAL_NODE_EXCHANGE = 'obnl.local.node.'
    """Base of every local exchange (followed by the name of the Node)"""

    SIMULATION_NODE_QUEUE = 'obnl.simulation.node.'
    """Base of every update queue (followed by the name of the Node)"""
    SIMULATION_NODE_EXCHANGE = 'obnl.simulation.node.'
    """Base of every update exchange (followed by the name of the Node)"""

    DATA_NODE_QUEUE = 'obnl.data.node.'
    """Base of every data queue (followed by the name of the Node)"""
    DATA_NODE_EXCHANGE = 'obnl.data.node.'
    """Base of every data/attr exchange (followed by the name of the Node)"""

    UPDATE_ROUTING = 'obnl.update.block.'
    """Base of every routing key for block messages (followed by the number/position of the block)"""

    def __init__(self, host, name):
        """
        The constructor creates the 3 main queues
        - general: To receive data with everyone
        - update: To receive data for the time management
        - data: To receive attribute update

        :param host: the connection to AMQP
        :param name: the id of the Node
        """
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self._channel = connection.channel()
        self._name = name

        self._simulation_queue = self._channel.queue_declare(queue=Node.SIMULATION_NODE_QUEUE + self._name)
        self._simulation_exchange = self._channel.exchange_declare(exchange=Node.SIMULATION_NODE_EXCHANGE + self._name)

        self._channel.basic_consume(self.on_simulation_message,
                                    consumer_tag='obnl_node_' + self._name + '_simulation',
                                    queue=self._simulation_queue.method.queue,
                                    no_ack=True)

    @property
    def name(self):
        """

        :return: the name of the Node 
        """
        return self._name

    def start(self):
        """
        Starts listening.
        """
        self._channel.start_consuming()

    def on_local_message(self, ch, method, props, body):
        """
        Callback when a message come from this node.
        """
        raise NotImplementedError('Abstract function call from '+str(self.__class__))

    def on_simulation_message(self, ch, method, props, body):
        """
        Callback when a message come from another Node to inform about simulation.
        """
        raise NotImplementedError('Abstract function call from '+str(self.__class__))

    def on_data_message(self, ch, method, props, body):
        """
        Callback when a message come from another Node to inform about data update.
        """
        raise NotImplementedError('Abstract function call from '+str(self.__class__))

    def send(self, exchange, routing, message, reply_to=None):
        """
        
        :param exchange: the MQTT exchange
        :param routing: the MQTT routing key
        :param message: the protobuf message
        :param reply_to: the routing key to reply to
        """

        mm = MetaMessage()
        mm.node_name = self._name
        mm.details.Pack(message)

        self._channel.publish(exchange=exchange,
                              routing_key=routing,
                              properties=pika.BasicProperties(reply_to=reply_to),
                              body=mm.SerializeToString())

    def reply_to(self, reply_to, message):
        """
        Replies to a message.

        :param reply_to: the asker 
        :param message: the message (str)
        """
        if reply_to:
            m = MetaMessage()
            m.node_name = self._name
            m.type = MetaMessage.ANSWER

            m.details.Pack(message)

            self._channel.publish(exchange='', routing_key=reply_to, body=m.SerializeToString())

    def send_simulation(self, routing, message, reply_to=None):
        """

        :param routing: the MQTT routing key
        :param message: the protobuf message
        :param reply_to: the routing key to reply to
        """
        self.send(Node.SIMULATION_NODE_EXCHANGE + self._name,
                  routing, message, reply_to=reply_to)


class ClientNode(Node):

    def __init__(self, host, name, api, input_attributes=None, output_attributes=None, is_first=False):
        super(ClientNode, self).__init__(host, name)

        # Local communication
        self._local_queue = self._channel.queue_declare(queue=Node.LOCAL_NODE_QUEUE + self._name)
        self._local_exchange = self._channel.exchange_declare(exchange=Node.LOCAL_NODE_EXCHANGE + self._name)

        self._channel.basic_consume(self.on_local_message,
                                    consumer_tag='obnl_node_' + self._name + '_local',
                                    queue=self._local_queue.method.queue,
                                    no_ack=True)
        self._channel.queue_bind(exchange=Node.LOCAL_NODE_EXCHANGE + self._name,
                                 queue=Node.LOCAL_NODE_QUEUE + self._name)

        # Data communication
        self._data_queue = self._channel.queue_declare(queue=Node.DATA_NODE_QUEUE + self._name)

        self._channel.basic_consume(self.on_data_message,
                                    consumer_tag='obnl_node_' + self._name + '_data',
                                    queue=self._data_queue.method.queue,
                                    no_ack=True)

        self._api_node = api

        self._next_step = False
        self._reply_to = None
        self._is_first = is_first
        self._current_time = 0
        self._time_step = 0

        self._links = {}
        self._input_values = {}
        self._input_attributes = input_attributes
        self._output_attributes = output_attributes

        si = SimulatorConnection()
        si.type = SimulatorConnection.OTHER

        self.send_simulation(Node.SIMULATION_NODE_EXCHANGE + Node.SCHEDULER_NAME,
                             si, reply_to=Node.SIMULATION_NODE_QUEUE + self.name)

    @property
    def input_values(self):
        return self._input_values

    @property
    def input_attributes(self):
        return self._input_attributes

    @property
    def output_attributes(self):
        return self._output_attributes

    def step(self, current_time, time_step):
        self._api_node.step(current_time, time_step)

    def update_attribute(self, attr, value):
        """
        Sends the new attribute value to those who want to know.

        :param attr: the attribute to communicate 
        :param value: the new value of the attribute
        """
        am = AttributeMessage()
        am.simulation_time = self._current_time
        am.attribute_name = attr
        am.attribute_value = float(value)

        m = MetaMessage()
        m.node_name = self._name
        m.type = MetaMessage.ATTRIBUTE
        m.details.Pack(am)

        if self._output_attributes:
            self._channel.publish(exchange=Node.DATA_NODE_EXCHANGE + self._name,
                                  routing_key=Node.DATA_NODE_EXCHANGE + attr,
                                  body=m.SerializeToString())

    def on_local_message(self, ch, method, props, body):
        if self._next_step \
                and (self._is_first
                     or not self._input_attributes
                     or len(self._input_values.keys()) == len(self._input_attributes)):
            # TODO: call updateX or updateY depending on the meta content
            self.step(self._current_time, self._time_step)
            self._next_step = False
            self._input_values.clear()
            nm = NextStep()
            nm.current_time = self._current_time
            nm.time_step = self._time_step
            self.reply_to(self._reply_to, nm)

    def on_simulation_message(self, ch, method, props, body):
        mm = MetaMessage()
        mm.ParseFromString(body)

        if mm.details.Is(NextStep.DESCRIPTOR) and mm.node_name == Node.SCHEDULER_NAME:
            nm = NextStep()
            mm.details.Unpack(nm)
            self._next_step = True
            self._reply_to = props.reply_to
            self._current_time = nm.current_time
            self._time_step = nm.time_step
            self.send_local(mm.details)
        elif mm.details.Is(SchedulerConnection.DESCRIPTOR):
            sc = SchedulerConnection()
            mm.details.Unpack(sc)
            self._links = dict(sc.attribute_links)
        elif mm.details.Is(Quit.DESCRIPTOR):
            sys.exit(0)

    def on_data_message(self, ch, method, props, body):
        mm = MetaMessage()
        mm.ParseFromString(body)

        if mm.details.Is(AttributeMessage.DESCRIPTOR):
            am = AttributeMessage()
            mm.details.Unpack(am)
            self._input_values[self._links[am.attribute_name]] = am.attribute_value
        self.send_local(mm.details)

    def send_local(self, message):
        """
        Sends the content to local.

        :param message: a protobuf message 
        """
        self.send(Node.LOCAL_NODE_EXCHANGE + self._name,
                  Node.LOCAL_NODE_EXCHANGE + self._name,
                  message)

    def send_scheduler(self, message):
        """
        Sends the content to scheduler.

        :param message: a protobuf message 
        """
        self.send(Node.SIMULATION_NODE_EXCHANGE + self._name,
                  Node.SIMULATION_NODE_EXCHANGE + Node.SCHEDULER_NAME,
                  message)
