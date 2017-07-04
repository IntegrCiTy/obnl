import random
from obnl.client import ClientNode


class ClientTestNode(ClientNode):

    def __init__(self, host, name, input_attributes=None, output_attributes=None, is_first=False):
        super(ClientTestNode, self).__init__(host, name, input_attributes, output_attributes, is_first)

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

    a = ClientTestNode('localhost', 'A', output_attributes=['ta'], input_attributes=['seta'], is_first=True)
    b = ClientTestNode('localhost', 'B', output_attributes=['tb'])
    c = ClientTestNode('localhost', 'C', input_attributes=['t1', 't2'], output_attributes=['setc'])

    print('Start A')
    a.start()
    print('Start B')
    b.start()
    print('Start C')
    c.start()
