# -*- coding: utf-8 -*-

"""
    Provisioning script
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

from fabric.colors import red
from fabric.utils import puts
from fabric.api import env
from provision import settings

##
## Enviroments
##

def development():
    """ Setup for vagrant box """
    puts(red('-- Working in vagrant box'))
    username = settings["enviroments"]["development"]['BOX_USERNAME']
    password = settings["enviroments"]["development"]['BOX_PASSWORD']
    ip = settings["enviroments"]["development"]['BOX_IP']
    env.user = username
    env.hosts = ['%s:22' % ip]
    env.password = password


def staging():
    """ Setup for staging enviroment """ 
    puts(red('-- Working in staging enviroment'))
    username = settings["enviroments"]['staging']['USERNAME']
    hosts = settings["enviroments"]['staging']['HOSTS']
    public_key = settings["enviroments"]['staging']['PUBLIC_KEY_PATH']    
    env.username = username
    env.hosts = hosts
    env.key_filename = public_key


def production():
    """ Setup for production enviroment """    
    puts(red('-- Working in production enviroment'))   
    username = settings["enviroments"]['production']['USERNAME']    
    hosts = settings["enviroments"]['production']['HOSTS']
    public_key = settings["enviroments"]['production']['PUBLIC_KEY_PATH']    
    env.username = username    
    env.hosts = hosts
    env.key_filename = public_key
