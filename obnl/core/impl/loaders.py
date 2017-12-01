
class Loader(object):
    """
    Base class of every Loaders
    """

    def __init__(self, scheduler):
        """
        
        :param host: the scheduler 
        """
        self._scheduler = scheduler
        self._nodes = []
        self._links = []

    def get_nodes(self):
        """
        
        :return: the loaded nodes or an empty list 
        """
        return self._nodes

    def get_links(self):
        """
        
        :return: the loaded links or an empty list 
        """
        return self._links


class JSONLoader(Loader):
    """
    A JSON Loader that can load data which follows the structure:
    {
        "nodes":{
            "NodeName1":{
                "inputs": [list of inputs]
                "outputs": [list of outputs]
            },
            ...
        }
        "links":{
            "LinkName1":{
                "out":{
                    "node": "NameNodeN"  # MUST be is "nodes"
                    "attr": "AttributeName"
                },
                "in":{
                    "node": "NameNodeN"  # MUST be is "nodes"
                    "attr": "AttributeName"
                }
            },
            ...
        }
    }   
    """
    def __init__(self, scheduler, config_data):
        super(JSONLoader, self).__init__(scheduler)

        # load the nodes
        self._prepare_nodes(config_data['nodes'])
        # then the links
        self._prepare_links(config_data['links'])

    def _find_in_nodes(self, str_node):
        for node in self._nodes:
            if str_node == node:
                return node

    def _prepare_nodes(self, nodes):
        for name, data in nodes.items():
            self._nodes.append(name)

    def _prepare_links(self, links):

        for data in links:
            in_data = data["input"]
            out_data = data["output"]
            in_node = self._find_in_nodes(in_data['node'])
            if in_node is None:
                raise AttributeError("The input node "+in_data['node']+" is not initialised.")
            out_node = self._find_in_nodes(out_data['node'])
            if in_node is None:
                raise AttributeError("The out node "+out_data['node']+" is not initialised.")

            self._scheduler.create_data_link(out_node, out_data['attribute'], in_node, in_data['attribute'])
