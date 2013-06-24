# -*- coding: utf-8 -*-

"""
    Provisioning script
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

import cuisine
from fabric.colors import red, green
from fabric.utils import puts

# Import recipes here
from recipes import setup, python, nginx, uwsgi, postgres, git


##
## Configure host 
##
def configure_host():
    """ Configure host with recipes """
    puts(red('-- Configuring host '))    
    puts(green('### Start host configuration  ###'))

    ## Basic setup 
    setup.install()
    setup.config()

    # Call recipeshere
    # Comment/uncomment examples

    python.install()
    python.config()    
    nginx.install()
    uwsgi.install()
    postgres.install()
    git.install()
    git.config()


##
## Update packages database 
##
def update_host():
    """ Update packages database"""

    puts(red('-- Updating packages database'))
    cuisine.package_update()


##
## Upgrade packages 
##
def upgrade_host():
    """ Upgrade system"""

    puts(red('-- Upgrading packages'))
    cuisine.package_upgrade()
