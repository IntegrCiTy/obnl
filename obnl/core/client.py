from obnl.core.impl.logs import logger
from threading import Thread

from obnl.core.impl.node import ClientNode as _ClientNodeImpl


class ClientNode(object):

    def __init__(self, host, vhost, username, password, config_file, input_attributes=None, output_attributes=None, is_first=False):
        self._node_impl = _ClientNodeImpl(host, vhost, username, password, self, config_file, input_attributes, output_attributes, is_first)
        logger.debug("New ClientNode")

    @property
    def name(self):
        """
        
        :return: the node name. It is the ID of the Node inside the simulation
        """
        return self._node_impl.name

    @property
    def simulation(self):
        """
        :return: the simulation ID. Common to all nodes in a simulation (define by the scheduler)
        """
        return self._node_impl.simulation

    @property
    def input_values(self):
        """
        
        :return: a map of input values. The keys are the input attributes 
        """
        return self._node_impl.input_values

    @property
    def input_attributes(self):
        """
        
        :return: the list of input attributes 
        """
        return self._node_impl.input_attributes

    @property
    def output_attributes(self):
        """
        
        :return: the list of output attributes 
        """
        return self._node_impl.output_attributes

    def start(self):
        """
        Starts the listening
        """
        logger.debug("{} starts listening (new Thread)".format(self.name))
        Thread(target=self._node_impl.start).start()

    def step(self, current_time, time_step):
        """
        Abstract function to be implemented by children.
        This function is called once per Node per simulation step.
        
        :param current_time: the current time of the simulation
        :param time_step: the time step from the last call of this function
        """
        raise NotImplementedError('Abstract function call from '+str(self.__class__))

    def update_attribute(self, attr, value):
        """
        Sends the new attribute value to those who want to know.

        :param attr: the attribute to communicate 
        :param value: the new value of the attribute
        """
        self._node_impl.update_attribute(attr, value)
        logger.debug("{} send attribute {} update {}".format(self.name, attr, value))
