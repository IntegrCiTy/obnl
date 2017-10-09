import logging
import logging.handlers

from obnl.impl import node as _node


def activate_console_logging(log_level=logging.INFO):
    if not hasattr(activate_console_logging, "handler"):
        activate_console_logging.handler = logging.StreamHandler()
        _add_handler(activate_console_logging.handler, log_level)


def deactivate_console_logging():
    if hasattr(activate_console_logging, "handler"):
        _remove_handler(activate_console_logging.handler)
        del activate_console_logging.handler


def activate_file_logging(filename, log_level=logging.INFO):
    if not hasattr(activate_file_logging, "handler"):
        activate_file_logging.handler = logging.handlers.TimedRotatingFileHandler(filename)
        _add_handler(activate_file_logging.handler, log_level)


def deactivate_file_logging():
    if hasattr(activate_file_logging, "handler"):
        _remove_handler(activate_file_logging.handler)
        del activate_file_logging.handler


def _add_handler(handler, log_level):
    handler.setLevel(log_level)
    handler.setFormatter(logging.Formatter(_node.Node.DEFAULT_LOGGING_FORMAT))
    _node.Node.LOGGER.setLevel(1)  # TODO log all data
    _node.Node.LOGGER.addHandler(handler)


def _remove_handler(handler):
    _node.Node.LOGGER.removeHandler(handler)