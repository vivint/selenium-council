#! /usr/bin/env python
# -*- coding: utf-8 -*-
# >>
#     vivint-selenium-docker, 2017
# <<

__author__ = 'Blake VandeMerwe'
__version__ = '0.2.1'
__license__ = 'MIT'
__contact__ = 'blake.vandemerwe@vivint.com'
__url__ = 'https://source.vivint.com/projects/DEVOPS/repos/vivint-selenium-docker'

import logging

from gevent.monkey import patch_socket

from selenium_docker.drivers import (
    ChromeDriver,
    DockerDriver,
    FirefoxDriver
)
from selenium_docker.pool import DriverPool
from selenium_docker.proxy import SquidProxy


__all__ = [
    'ChromeDriver',
    'DockerDriver',
    'DriverPool',
    'FirefoxDriver',
    'SquidProxy'
]

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

patch_socket()
