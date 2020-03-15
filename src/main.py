#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""TBC
"""

from cli_interface import arg_parser
from cli_interface import prepare_url


def wrapper():
    """TBC
    """
    user_input = arg_parser()

    prepare_url(user_input)

if __name__ == "__main__":
    wrapper()
