import argparse
import logging

from obnl.util import convert_json_file_to_data
from obnl.impl.server import Scheduler

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("host")
    parser.add_argument("config_file")
    parser.add_argument("schedule_file")

    args = parser.parse_args()

    config_data = convert_json_file_to_data(args.config_file)
    schedule_data = convert_json_file_to_data(args.schedule_file)

    c = Scheduler(args.host, 'obnl_vhost', 'obnl', 'obnl', 'scheduler.json', config_data, schedule_data,
                  log_level=logging.DEBUG)
    c.start()
