from threading import Thread
from obnl.impl.node import ClientNode as _ClientNodeImpl


class ClientNode(object):

    def __init__(self, host, name, input_attributes=None, output_attributes=None, is_first=False):
        self._node_impl = _ClientNodeImpl(host, name, self, input_attributes, output_attributes, is_first)

    @property
    def name(self):
        """
        
        :return: the node name. It is the ID of the Node inside the simulation 
        """
        return self._node_impl.name

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
