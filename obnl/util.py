import json


def convert_json_to_data(json_text):
    return json.loads(json_text)


def convert_json_file_to_data(schedule_file):
    with open(schedule_file) as json_file:
        schedule_data = convert_json_to_data(json_file.read())
    return schedule_data
