# -*- coding: utf-8 -*-

"""
    Provisioning and deploy in remote servers
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

import cuisine
from fabric.api import env
from provision import update_host, upgrade_host, configure_host
from provision.recipes import git, postgres 

##
## Remote enviroments
##

def vagrant():
    """ Setup for vagrant box """
    env.hosts = ['nekro@192.168.50.4']

def staging():
    """ Setup for staging enviroments """    
    env.hosts = ['nekro@192.168.50.4:22']

def production():
    """ Setup for production enviroments """    
    env.hosts = ['nekro@192.168.50.4:22']


##
## Deploy and remote tasks for remote hosts
##

def configure_git():
    """ Config gitolite """    
    git.config()

def create_user():
    """ Create postgres user """    
    postgres.create_user()

def create_db():
    """ Create postgres database """    
    postgres.create_db()

