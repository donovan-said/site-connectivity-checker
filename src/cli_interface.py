#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""TBC
"""


import logging
import argparse


HTTP = "http://"
""" HTTP
"""

HTTPS = "https://"
""" HTTPS
"""

LOGGER = logging.getLogger()
""" LOGGER
"""

LOGGER.setLevel(logging.DEBUG)

def user_interface():
    """TBC
    """
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('--url', action='store', type=str, required=True,
                           help="The URL that you want to test.")

    args = my_parser.parse_args()

    return args

print(user_interface())
