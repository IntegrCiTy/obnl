import logging
import random

from obnl.client import ClientNode


class ClientTestNode(ClientNode):

    def __init__(self, host, vhost, username, password, config_file,
                 input_attributes=None, output_attributes=None, is_first=False):
        super().__init__(host, vhost, username, password, config_file,
                         input_attributes, output_attributes, is_first)
        self._node_impl.activate_console_logging(logging.DEBUG)

    def step(self, current_time, time_step):
        print('----- '+self.name+' -----')
        print(self.name, time_step)
        print(self.name, current_time)
        print(self.name, self.input_values)

        for o in self.output_attributes:
            rv = random.random()
            print(self.name, o, ':', rv)
            self.update_attribute(o, rv)
        print('=============')


if __name__ == "__main__":

    a = ClientTestNode('localhost', 'obnl_vhost', 'obnl', 'obnl', 'A.json',
                       output_attributes=['ta'], input_attributes=['seta'], is_first=True)
    b = ClientTestNode('localhost', 'obnl_vhost', 'obnl', 'obnl', 'B.json',
                       output_attributes=['tb'])
    c = ClientTestNode('localhost', 'obnl_vhost', 'obnl', 'obnl', 'C.json',
                       input_attributes=['t1', 't2'], output_attributes=['setc'])

    a.start()
    b.start()
    c.start()
