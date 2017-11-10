import json

from google.protobuf import json_format

from message.coside.coside_pb2 import SimulationInit, Schedule


def convert_json_to_data(json_text):
    return json.loads(json_text)


def convert_json_file_to_data(json_file_location):
    with open(json_file_location) as json_file:
        schedule_data = convert_json_to_data(json_file.read())
    return schedule_data


def convert_protobuf_to_data(message):
    if type(message) is SimulationInit:
        data = json.loads(json_format.MessageToJson(message, preserving_proto_field_name=True))
        res = dict()
        res['links'] = data['links']
        res['nodes'] = {}
        for node in data['nodes']:
            res['nodes'][node['name']] = {
                'inputs': node['inputs'] if 'inputs' in node else None,
                'outputs': node['outputs'] if 'outputs' in node else None
            }
        return res
    elif type(message) is Schedule:
        return json.loads(json_format.MessageToJson(message, preserving_proto_field_name=True))
    else:
        return json.loads(json_format.MessageToJson(message, preserving_proto_field_name=True))
