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
    """ Install git packages """

    puts(green('-> Installing gitolite'))
    cuisine.package_ensure('gitolite')
        
    puts(green('-> Creating git user'))
    cuisine.user_ensure('git')

    puts(green('-> Uploading admin public key'))  
    public_key = raw_input('Enter path of your public key: ')
    cuisine.file_upload('/tmp/admin.pub', public_key)
    
    puts(green('-> Configuring gitolite'))
    puts(red('== Options for wizard '))
    puts(red('== user -> git '))
    puts(red('== path -> /home/git/ '))
    puts(red('== key -> /tmp/admin.pub '))
    raw_input('Press enter to continue') 
    cuisine.sudo('dpkg-reconfigure gitolite')
