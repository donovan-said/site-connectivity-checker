#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""TBC
"""

import logging
from cli_interface import arg_parser
from cli_interface import prepare_url
from conn_checker import conn_checker

LOGGER = logging.getLogger()
""" LOGGER
"""

# Setting log level.
LOGGER.setLevel(logging.DEBUG)


def wrapper():
    """TBC
    """

    user_input = arg_parser()
    url_endpoint = prepare_url(user_input)
    LOGGER.info('Attempting to connect to: %s ', url_endpoint)
    conn_checker(url_endpoint)

if __name__ == "__main__":
    wrapper()
