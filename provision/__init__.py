# -*- coding: utf-8 -*-

"""
    Provisioning script
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

import getpass
import cuisine
from fabric.colors import red, green
from fabric.utils import puts

# Import recipes here
from recipes import setup, python, nginx, uwsgi, postgres, git


DEFAULT_USERNAME = 'nekro'

##
## Configure host
##
def configure_host():
    """ Configure host with recipes """

    puts(red('-- Configuring host '))    
    puts(green('--> Start host configuration'))
    username = DEFAULT_USERNAME
    password = getpass.getpass('Enter your password: ')
    public_key = raw_input('Public key path (Press enter to ignore): ')

    ## Basic setup 
    setup.install(username, password, public_key)

    # Call recipeshere
    # Comment/uncomment examples

    python.install()
    nginx.install()
    uwsgi.install()
    postgres.install()
    git.install()


##
## Packages update & upgrade
##
def update_host():
    """ Update packages database"""

    puts(red('-- Updating packages database'))
    cuisine.package_update()

def upgrade_host():
    """ Upgrade system"""

    puts(red('-- Upgrading packages'))
    cuisine.package_upgrade()


##
## Git
##
def configure_git():
    """ Config gitolite """ 
    puts(red('-- Gitolite setup'))   
    public_key = raw_input('Public key path: ')    
    git.config(public_key)


##
## Postgres 
##
def create_pg_user_db():
    """ Create postgres user """   
    puts(red('-- Postgres setup'))       
    username = raw_input('Username for database: ')   
    db = raw_input('Name for database: ')        
    postgres.create_user(username)
    postgres.create_db(db, username)


##
## Nginx 
##
def create_nginx_vhost():
    """ Create nginx vhost """    
    pass


##
## Uwsgi
##
def create_uwsgi_app():
    """ Create uwsgi app """    
    pass

