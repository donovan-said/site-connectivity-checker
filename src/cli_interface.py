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

# Setting log level.
LOGGER.setLevel(logging.DEBUG)

def arg_parser():
    """A function to manage cli arguments.

    Arguments:
        None.

    Returns:
        User input.
    """
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('--url', action='store', type=str, required=True,
                           help="The URL that you want to test.")
    my_parser.add_argument('--port', action='store', type=str, required=False,
                           help="The port associated to the endpoint.")

    args = my_parser.parse_args()

    return args

if __name__ == "__main__":
    pass
