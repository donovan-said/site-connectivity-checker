#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""TBC
"""

import logging
import urllib.request
import urllib.error

LOGGER = logging.getLogger()
""" LOGGER
"""

# Setting log level.
LOGGER.setLevel(logging.DEBUG)


def conn_checker(url_endpoint):
    """TBC
    """

    url = url_endpoint
    try:
        urllib.request.urlopen(url)
    except urllib.error.HTTPError as http_error:
        LOGGER.error('HTTP Error: %s', http_error.code)
    except urllib.error.URLError as http_error:
        # Not a HTTP specific error
        LOGGER.error('Non HTTP Error: %s', http_error.reason)
    else:
        LOGGER.info('Connection Returned 200.')
        print('200')


if __name__ == "__main__":
    pass
