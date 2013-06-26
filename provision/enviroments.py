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
    username = settings['vagrant']['BOX_USERNAME']
    password = settings['vagrant']['BOX_PASSWORD']
    ip = settings['vagrant']['BOX_IP']
    env.hosts = ['%s@%s:22' % (username, ip)]
    env.password = password


def staging():
    """ Setup for staging enviroment """ 
    puts(red('-- Working in staging enviroment')) 
    hosts = settings['staging']['HOSTS']
    public_key = settings['staging']['HOSTS']    
    env.hosts = hosts
    env.key_filename = public_key


def production():
    """ Setup for production enviroment """    
    puts(red('-- Working in production enviroment'))        
    hosts = settings['production']['HOSTS']
    public_key = settings['production']['HOSTS']    
    env.hosts = hosts
    env.key_filename = public_key
