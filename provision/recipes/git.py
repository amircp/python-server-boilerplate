# -*- coding: utf-8 -*-

"""
    GIT recipe
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
    puts(green('-> Installing gitolite'))
    cuisine.package_ensure('gitolite')
        
    puts(green('-> Creating git user'))
    cuisine.user_ensure('git')


##
## Tasks for remote hosts
##
def config():
    """ Config gitolite """

    puts(green('-> Uploading admin public key'))    
    admin_key = raw_input('SSH public key path: ')
    cuisine.file_upload('/tmp/admin.pub', admin_key)
    
    # Launch gitolite config
    puts(green('-> Configure gitolite'))
    puts(red('== Options '))
    puts(red('== user -> git '))
    puts(red('== path -> /home/git/ '))
    puts(red('== key -> /tmp/admin.pub '))
    raw_input('Press enter to continue') 
    cuisine.sudo('dpkg-reconfigure gitolite')
