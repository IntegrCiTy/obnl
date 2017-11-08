import argparse
import logging

from obnl.impl.server import Scheduler

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("host")
    parser.add_argument("config_file")
    parser.add_argument("schedule_file")

    args = parser.parse_args()

    c = Scheduler(args.host, 'obnl_vhost', 'obnl', 'obnl', 'scheduler.json', args.config_file, args.schedule_file,
                  log_level=logging.DEBUG)
    c.start()
