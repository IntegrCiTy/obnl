import sys
import json

from obnl.impl.node import Node
from obnl.impl.loaders import JSONLoader
from obnl.impl.message import SimulatorConnection, NextStep, MetaMessage, SchedulerConnection, Quit


class Scheduler(Node):
    """
    The Scheduler is a Node that manage the time flow.
    """

    def __init__(self, host, config_file, schedule_file):
        """
        
        :param host: the AMQP host 
        :param config_file: a file containing time steps
        :param schedule_file: a file containing schedule blocks
        """
        super(Scheduler, self).__init__(host, Node.SCHEDULER_NAME)
        self._current_step = 0
        self._current_block = 0

        self._connected = set()
        self._sent = set()
        self._links = {}

        self._channel.exchange_declare(exchange=Node.SIMULATION_NODE_EXCHANGE + self._name)

        self._steps, self._blocks = self._load_data(config_file, schedule_file)

        self._current_time = 0

    def _load_data(self, config_file, schedule_file):
        """
        :param config_file: the file containing the structure
        :param schedule_file: the file containing the schedule 
        """

        # Currently only JSON can be loaded
        with open(schedule_file) as jsonfile:
            schedule_data = json.loads(jsonfile.read())
            steps = schedule_data['steps']
            blocks = schedule_data['schedule']

        # Currently only JSON can be loaded
        # Load all the Nodes and creates the associated links
        loader = JSONLoader(self, config_file)
        # Connects the created Nodes to the update exchanger
        # using the schedule definition (blocks)
        # TODO: Should it be in Creator or Scheduler ???
        for node in loader.get_nodes():
            i = 0
            for block in blocks:
                if node in block:
                    self.create_simulation_links(node, i)
                i += 1
        return steps, blocks

    def start(self):
        """
        Starts listening.
        """
        self._current_step = 0
        self._current_block = 0
        super(Scheduler, self).start()

    def create_data_link(self, node_out, attr_out, node_in, attr_in):
        """
        Creates and connects the attribute communication from Node to Node.

        :param node_out: the Node sender name
        :param attr_out: the name of the attribute the Node want to communicate
        :param node_in: the Node receiver name
        :param attr_in: the name of the attribute from the Node receiver point of view
        """
        self._channel.exchange_declare(exchange=Node.DATA_NODE_EXCHANGE + node_out)
        self._channel.queue_declare(queue=Node.DATA_NODE_QUEUE + node_in)

        self._channel.queue_bind(exchange=Node.DATA_NODE_EXCHANGE + node_out,
                                 routing_key=Node.DATA_NODE_EXCHANGE + attr_out,
                                 queue=Node.DATA_NODE_QUEUE + node_in)
        if node_in not in self._links:
            self._links[node_in] = {}
        self._links[node_in][attr_out] = attr_in

    def create_simulation_links(self, node, position):
        """
        Connects the scheduler exchange to the update queue of the Node

        :param node: the node to be connected to
        :param position: the position of the containing block
        """
        self._channel.exchange_declare(exchange=Node.SIMULATION_NODE_EXCHANGE + self._name)
        self._channel.queue_declare(queue=Node.SIMULATION_NODE_QUEUE + node)
        self._channel.queue_bind(exchange=Node.SIMULATION_NODE_EXCHANGE + self._name,
                                 routing_key=Node.UPDATE_ROUTING + str(position),
                                 queue=Node.SIMULATION_NODE_QUEUE + node)

        self._channel.exchange_declare(exchange=Node.SIMULATION_NODE_EXCHANGE + node)
        self._channel.queue_declare(queue=Node.SIMULATION_NODE_QUEUE + self._name)
        self._channel.queue_bind(exchange=Node.SIMULATION_NODE_EXCHANGE + node,
                                 routing_key=Node.SIMULATION_NODE_EXCHANGE + self._name,
                                 queue=Node.SIMULATION_NODE_QUEUE + self._name)

    def _update_time(self):
        """
        Sends new time message to the current block. 
        """
        ns = NextStep()
        ns.time_step = self._steps[self._current_step]
        ns.current_time = self._current_time

        self.send_simulation(Node.UPDATE_ROUTING + str(self._current_block),
                             ns, reply_to=Node.SIMULATION_NODE_QUEUE + self.name)

    def on_local_message(self, ch, method, props, body):
        """
        Callback when a message come from this node. Never append with Scheduler
        """
        pass

    def on_simulation_message(self, ch, method, props, body):
        """
        Callback when a message come from Node.
        """
        m = MetaMessage()
        m.ParseFromString(body)

        if m.details.Is(SimulatorConnection.DESCRIPTOR):
            self._simulator_connection(m, props.reply_to)
            if len(self._connected) == sum([len(b) for b in self._blocks]):
                self._current_time += self._steps[self._current_step]
                self._update_time()

        if m.details.Is(NextStep.DESCRIPTOR):
            if m.node_name in self._blocks[self._current_block]:
                self._sent.add(m.node_name)

        if len(self._connected) == sum([len(b) for b in self._blocks]):
            # block management
            if len(self._sent) == len(self._blocks[self._current_block]):
                self._current_block = (self._current_block + 1) % len(self._blocks)
                if self._current_block == 0:
                    self._current_step += 1
                    if self._current_step >= len(self._steps):
                        self.broadcast_simulation(Quit())
                        sys.exit(0)
                    else:
                        self._current_time += self._steps[self._current_step]
                self._update_time()
                self._sent.clear()

    def _simulator_connection(self, message, reply_to):
        node_name = message.node_name
        self._connected.add(node_name)

        sc = SchedulerConnection()
        if node_name in self._links:
            for k, v in self._links[node_name].items():
                sc.attribute_links[k] = v

        self.reply_to(reply_to, sc)

    def on_data_message(self, ch, method, props, body):
        """
        Displays message receive from the data queue.
        """
        pass

    def broadcast_simulation(self, message, reply_to=None):

        for block_id in range(len(self._blocks)):
            self.send_simulation(Node.UPDATE_ROUTING + str(block_id),
                                 message, reply_to=reply_to)

