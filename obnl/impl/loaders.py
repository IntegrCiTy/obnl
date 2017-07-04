import json


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
    def __init__(self, scheduler, config_file):
        super(JSONLoader, self).__init__(scheduler)

        # load the data from json file
        with open(config_file) as jsonfile:
            config_data = json.loads(jsonfile.read())

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

        for name, data in links.items():
            in_data = data["in"]
            out_data = data["out"]
            in_node = self._find_in_nodes(in_data['node'])
            out_node = self._find_in_nodes(out_data['node'])

            self._scheduler.create_data_link(out_node, out_data['attr'], in_node, in_data['attr'])
