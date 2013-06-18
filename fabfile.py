# -*- coding: utf-8 -*-

"""
    Setup for provisioning remote servers
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

from fabric.api import env
from provisioning import configure_host


def staging():
    env.hosts = []

def production():
    env.hosts = []


