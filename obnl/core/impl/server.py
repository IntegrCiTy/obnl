import logging
import logging.handlers
import time

from obnl.core.impl.loaders import JSONLoader
from obnl.core.impl.node import Node

from ict.protobuf.core_pb2 import MetaMessage
from ict.protobuf.obnl_pb2 import *


class Scheduler(Node):
    """
    The Scheduler is a Node that manage the time flow.
    """

    def __init__(self, host, vhost, username, password, config_file,
                 simu_data, schedule_data,
                 log_level=logging.INFO):
        """
        
        :param host: the AMQP host 
        :param config_file: a file containing queues & exchanges
        :param simu_data: a dict containing connections
        :param schedule_data: a dict containing schedule blocks
        """
        self.activate_console_logging(log_level)
        super(Scheduler, self).__init__(host, vhost, username, password, config_file)

        self._current_step = 0
        self._current_block = 0

        self._connected = set()
        self._sent = set()
        self._links = {}

        self._begin_time = 0

        self._steps, self._blocks = self._load_data(simu_data, schedule_data)

        self._current_time = 0

    def _load_data(self, config_data, schedule_data):
        """
        :param config_data: the structure as a dict
        :param schedule_data: the schedule as a dict
        """

        # Currently only JSON can be loaded
        steps = schedule_data['steps']
        blocks = schedule_data['schedule']
        self._simulation = schedule_data['simulation_name']
        Scheduler.LOGGER.debug("Simulation '" + str(self.simulation) + "' loaded")

        # Currently only JSON can be loaded
        # Load all the Nodes and creates the associated links
        loader = JSONLoader(self, config_data)
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
        Creates and connects the attribute communication from Node to Scheduler.

        :param node_out: the Node sender name
        :param attr_out: the name of the attribute the Node want to communicate
        :param node_in: the Node receiver name
        :param attr_in: the name of the attribute from the Node receiver point of view
        """
        self._channel.queue_declare(queue=Scheduler.DATA + node_in)
        self._channel.exchange_declare(exchange=Scheduler.DATA + node_out)
        self._channel.queue_bind(exchange=Scheduler.DATA + node_out,
                                 routing_key=Scheduler.DATA + attr_out,
                                 queue=Scheduler.DATA + node_in)
        if node_in not in self._links:
            self._links[node_in] = {}
        self._links[node_in][attr_out] = attr_in

    def create_simulation_links(self, node, position):
        """
        Connects the scheduler exchange to the update queue of the Node

        :param node: the node to be connected to
        :param position: the position of the containing block
        """
        self._channel.queue_declare(queue=Scheduler.SIMULATION + node)
        self._channel.exchange_declare(exchange=Scheduler.SIMULATION + self.name)
        self._channel.queue_bind(exchange=Scheduler.SIMULATION + self.name,
                                 routing_key=Scheduler.UPDATE_ROUTING + str(position),
                                 queue=Scheduler.SIMULATION + node)

        self._channel.queue_declare(queue=Scheduler.SIMULATION + self._name)
        self._channel.queue_bind(exchange=Scheduler.SIMULATION + self.name,
                                 routing_key=Scheduler.SIMULATION + self._name,
                                 queue=Scheduler.SIMULATION + self._name)

    def _update_time(self):
        """
        Sends new time message to the current block. 
        """
        ns = NextStep()
        ns.time_step = self._steps[self._current_step]
        ns.current_time = self._current_time
        Scheduler.LOGGER.debug("Current step is " + str(self._current_time))

        self.send_simulation(Scheduler.UPDATE_ROUTING + str(self._current_block),
                             ns, reply_to=Scheduler.SIMULATION + self.name)

    def on_simulation(self, ch, method, props, body):
        """
        Callback when a message come from Scheduler.
        """
        m = MetaMessage()
        m.ParseFromString(body)

        if m.details.Is(SimulatorConnection.DESCRIPTOR):
            self._simulator_connection(m, props.reply_to)
            Scheduler.LOGGER.info("Simulator " + m.node_name + " is connected.")
            if len(self._connected) == sum([len(b) for b in self._blocks]):
                Scheduler.LOGGER.info("Start simulation.")
                self._begin_time = time.time()
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
                        Scheduler.LOGGER.info("Simulation finished. Execution time: " +
                                              str(time.time() - self._begin_time)
                                              + " seconds")
                        self._channel.basic_ack(delivery_tag=method.delivery_tag)
                        sys.exit(0)
                    else:
                        self._current_time += self._steps[self._current_step]
                self._update_time()
                self._sent.clear()

        self._channel.basic_ack(delivery_tag=method.delivery_tag)

    def _simulator_connection(self, message, reply_to):
        node_name = message.node_name
        self._connected.add(node_name)

        sc = SchedulerConnection()
        sc.simulation = self._simulation
        if node_name in self._links:
            for k, v in self._links[node_name].items():
                sc.attribute_links[k] = v

        self.reply_to(reply_to, sc)

    def broadcast_simulation(self, message, reply_to=None):

        for block_id in range(len(self._blocks)):
            self.send_simulation(Scheduler.UPDATE_ROUTING + str(block_id), message, reply_to=reply_to)
