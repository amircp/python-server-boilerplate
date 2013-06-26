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

    puts(green('-> Configre postgres user login'))    
    old_srt = "local   all             all                                     peer"
    new_srt = "local   all             all                                     trust"
    cuisine.sudo('sed -i "s/%s/%s/g" /etc/postgresql/9.2/main/pg_hba.conf' % (old_srt, new_srt))
    cuisine.sudo('/etc/init.d/postgresql restart')
    

##
## Tasks for remote hosts
##
def create_user(username):
    """ Create user """

    # Launch gitolite config
    puts(green('-> Creating postgres username'))
    cuisine.sudo('createuser -d -l -R -E -W %s' % username, user='postgres')

def create_db(db, username):
    """ Create user and database """

    # Launch gitolite config
    puts(green('-> Creating postgres database'))
    cuisine.sudo('psql -c "CREATE DATABASE %s;"' % db, user='postgres')
    cuisine.sudo('psql -c "GRANT ALL PRIVILEGES ON DATABASE %s to %s;"' % (db, username), user='postgres')

