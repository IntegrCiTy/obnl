import logging
import argparse

import obnl.logger
from obnl.impl.server import Scheduler

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("host")
    parser.add_argument("config_file")
    parser.add_argument("schedule_file")

    args = parser.parse_args()

    obnl.logger.activate_console_logging()

    c = Scheduler(args.host, args.config_file, args.schedule_file, log_level=logging.DEBUG)
    c.start()
