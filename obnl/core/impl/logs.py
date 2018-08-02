#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from logging.handlers import RotatingFileHandler

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

file_formatter = logging.Formatter("%(asctime)s :: %(levelname)s :: %(pathname)s :: %(funcName)s :: %(message)s")

file_handler = RotatingFileHandler("activity.log", "w")

file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

stream_formatter = logging.Formatter("%(asctime)s :: %(levelname)s :: %(message)s")

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(stream_formatter)
logger.addHandler(stream_handler)
