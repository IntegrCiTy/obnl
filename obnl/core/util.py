import json


def convert_json_to_data(json_text):
    return json.loads(json_text)


def convert_json_file_to_data(json_file_location):
    with open(json_file_location) as json_file:
        schedule_data = convert_json_to_data(json_file.read())
    return schedule_data
