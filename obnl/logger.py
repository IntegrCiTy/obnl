import logging
import logging.handlers

from obnl.impl import node as _node


def activate_console_logging(log_level=logging.INFO):
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(logging.Formatter(_node.Node.DEFAULT_LOGGING_FORMAT))
    _node.Node.LOGGER.setLevel(1)  # TODO log all data
    _node.Node.LOGGER.addHandler(console_handler)


def activate_file_logging(filename, log_level=logging.INFO):
    file_handler = logging.handlers.TimedRotatingFileHandler(filename)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(logging.Formatter(_node.Node.DEFAULT_LOGGING_FORMAT))
    _node.Node.LOGGER.setLevel(1)  # TODO log all data
    _node.Node.LOGGER.addHandler(file_handler)
