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
    username = settings["enviroments"]["development"]['USERNAME']
    ip = settings["enviroments"]["development"]['IP']
    private_key = settings["enviroments"]['development']['VAGRANT_PRIVATE_KEY_PATH']       
    env.name = 'development'
    env.user = username
    env.hosts = ['%s:22' % ip]
    env.password = settings["enviroments"]['development']['PASSWORD']
    env.key_filename = private_key


def staging():
    """ Setup for staging enviroment """ 
    puts(red('-- Working in staging enviroment'))
    username = settings["enviroments"]['staging']['USERNAME']
    hosts = settings["enviroments"]['staging']['HOSTS']
    private_key = settings["enviroments"]['staging']['PRIVATE_KEY_PATH']    
    env.name = 'staging'    
    env.user = username
    env.hosts = hosts
    env.key_filename = private_key


def production():
    """ Setup for production enviroment """    
    puts(red('-- Working in production enviroment'))   
    username = settings["enviroments"]['production']['USERNAME']    
    hosts = settings["enviroments"]['production']['HOSTS']
    private_key = settings["enviroments"]['production']['PRIVATE_KEY_PATH']    
    env.name = 'production'    
    env.user = username    
    env.hosts = hosts
    env.key_filename = private_key
