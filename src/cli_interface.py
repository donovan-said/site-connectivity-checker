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


def prepare_url(argparse_input):
    """A function to modify user input into a functional URL.

    Arguments:

    Returns:
    """

    # Turn argparse Namespace into Dict
    user_input = vars(argparse_input)
    # Get url key value
    url_input = user_input.get('url')
    # Prepend HTTP
    url_full = HTTPS + url_input

    return url_full

if __name__ == "__main__":
    USER_INPUT = arg_parser()

    prepare_url(USER_INPUT)
