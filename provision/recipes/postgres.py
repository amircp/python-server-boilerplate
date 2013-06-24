# -*- coding: utf-8 -*-

"""
    Postgres recipe
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

import cuisine
from fabric.colors import red, green
from fabric.utils import puts


##
## Install packages 
##
def install():
    """ Install packages """

    # Install packages
    puts(green('-> Installing postgres'))
    if not cuisine.dir_exists('/etc/postgresql'):
        cuisine.sudo('echo "deb http://apt.postgresql.org/pub/repos/apt/ wheezy-pgdg main" > /etc/apt/sources.list.d/pgdg.list')
        cuisine.sudo('wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | sudo apt-key add -') 
        cuisine.package_update()
    cuisine.package_ensure('postgresql')
    cuisine.package_ensure('postgresql-server-dev-9.2')
    

##
## Tasks for remote hosts
##
def create_user():
    """ Create user """

    # Launch gitolite config
    puts(green('-> Creating user'))
    db_user = raw_input('New username: ')
    cuisine.sudo('createuser -d -l -R -E -W %s' % db_user, user='postgres')

def create_db():
    """ Create user """

    # Launch gitolite config
    puts(green('-> Creating user'))
    db_name = raw_input('Database name: ')
    db_user = raw_input('User owner: ')
    cuisine.sudo('psql -c "CREATE DATABASE %s;"' % db_name, user='postgres')
    cuisine.sudo('psql -c "GRANT ALL PRIVILEGES ON DATABASE %s to %s;"' % (db_name, db_user), user='postgres')

