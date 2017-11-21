from ict.connection.node import Node as ConnectionNode

from ict.protobuf.default_pb2 import MetaMessage
from ict.protobuf.obnl.core_pb2 import *


class Node(ConnectionNode):
    """
    This is the base class for all Nodes of the system. Improvement 
    """

    SCHEDULER_NAME = "scheduler"

    SIMULATION = "obnl.simulation.node."
    DATA = "obnl.data.node."
    LOCAL = "obnl.local.node."

    UPDATE_ROUTING = 'obnl.update.block.'
    """Base of every routing key for block messages (followed by the number/position of the block)"""

    def __init__(self, host, vhost, username, password, config_file="obnl.json"):
        """
        The constructor creates the 3 main queues
        - general: To receive data with everyone
        - update: To receive data for the time management
        - data: To receive attribute update

        :param host: the connection to RabbitMQ Server
        :param vhost: the virtual host of RabbitMQ Server
        :param username: the user connection
        :param password: the password connection
        :param config_file: the configuration file to generate queues & exchanges
        """
        super().__init__(host, vhost, username, password, config_file)
        self._simulation = None

    @property
    def simulation(self):
        return self._simulation

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

        super().send(exchange, routing, mm.SerializeToString(), reply_to)

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

            super().send(exchange='', routing=reply_to, message=m.SerializeToString())

    def send_simulation(self, routing, message, reply_to=None):
        """

        :param routing: the MQTT routing key
        :param message: the protobuf message
        :param reply_to: the routing key to reply to
        """
        self.LOGGER.debug('-->' + routing)
        self.send(Node.SIMULATION + self.name, routing, message, reply_to=reply_to)


class ClientNode(Node):

    def __init__(self, host, vhost, username, password, api, config_file="client.json", input_attributes=None, output_attributes=None, is_first=False):
        super(ClientNode, self).__init__(host, vhost, username, password, config_file)

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

        self.send_simulation(ClientNode.SIMULATION + 'scheduler', si, reply_to=ClientNode.SIMULATION + self.name)

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
            self._channel.publish(exchange=ClientNode.DATA + self._name,
                                  routing_key=ClientNode.DATA + attr,
                                  body=m.SerializeToString())

    def on_local(self, ch, method, props, body):
        if self._next_step \
                and (self._is_first
                     or not self._input_attributes
                     or len(self._input_values.keys()) == len(self._input_attributes)):
            # TODO: call updateX or updateY depending on the meta content
            Node.LOGGER.debug(self.name+" step running.")
            self.step(self._current_time, self._time_step)
            self._next_step = False
            self._input_values.clear()
            nm = NextStep()
            nm.current_time = self._current_time
            nm.time_step = self._time_step
            self.reply_to(self._reply_to, nm)

        self._channel.basic_ack(delivery_tag=method.delivery_tag)

    def on_simulation(self, ch, method, props, body):
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
            self._simulation = sc.simulation
            self._links = dict(sc.attribute_links)
            Node.LOGGER.debug(self.name + " connected to simulation '" + self.simulation+"'")
        elif mm.details.Is(Quit.DESCRIPTOR):
            Node.LOGGER.info(self.name+" disconnected!")
            self._channel.basic_ack(delivery_tag=method.delivery_tag)
            sys.exit(0)

        self._channel.basic_ack(delivery_tag=method.delivery_tag)

    def on_data(self, ch, method, props, body):
        mm = MetaMessage()
        mm.ParseFromString(body)

        if mm.details.Is(AttributeMessage.DESCRIPTOR):
            am = AttributeMessage()
            mm.details.Unpack(am)
            self._input_values[self._links[am.attribute_name]] = am.attribute_value
        self.send_local(mm.details)

        self._channel.basic_ack(delivery_tag=method.delivery_tag)

    def send_local(self, message):
        """
        Sends the content to local.

        :param message: a protobuf message 
        """
        self.send('', ClientNode.LOCAL + self._name, message)

    def send_scheduler(self, message):
        """
        Sends the content to scheduler.

        :param message: a protobuf message 
        """
        self.send('', ClientNode.SIMULATION + Node.SCHEDULER_NAME, message)
