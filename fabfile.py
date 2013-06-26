# -*- coding: utf-8 -*-

"""
    Provisioning and deploy in remote servers
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

import cuisine
from fabric.api import env
from provision import *


##
## Remote enviroments
##

def vagrant():
    """ Setup for vagrant box """
    env.hosts = ['vagrant@192.168.13.37:22']
    env.key_filename = ''

def staging():
    """ Setup for staging enviroments """    
    env.hosts = []
    env.key_filename = ''

def production():
    """ Setup for production enviroments """    
    env.hosts = []
    env.key_filename = ''
    


##
## Deploy and remote tasks for remote hosts
##
