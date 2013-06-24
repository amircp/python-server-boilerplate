# -*- coding: utf-8 -*-

"""
    Provisioning and deploy in remote servers
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

import cuisine
from fabric.api import env
from provision import update_host, upgrade_host, configure_host


##
## Remote enviroments
##

def devel():
    env.hosts = ['192.168.50.1']

def staging():
    env.hosts = ['192.168.50.1']

def production():
    env.hosts = ['192.168.50.1']


##
## Deploy and remote tasks for remote hosts
##
