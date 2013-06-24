# -*- coding: utf-8 -*-

"""
    Setup recipe
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

import getpass
import cuisine
from fabric.colors import red, green
from fabric.utils import puts


DEFAULT_USER = 'nekro'


##
## Install packages 
##
def install():
    """ Install packages """

    # Install packages
    puts(green('-> Installing nano'))
    cuisine.package_ensure("nano")
    
    puts(green('-> Installing VIM'))
    cuisine.package_ensure("vim")

    puts(green('-> Installing tmux'))
    cuisine.package_ensure("tmux")

    puts(green('-> Installing build-essential'))
    cuisine.package_ensure("build-essential")

    puts(green('-> Installing libxml2-dev'))
    cuisine.package_ensure("libxml2-dev")

    puts(green('-> Installing libjpeg8-dev'))
    cuisine.package_ensure("libjpeg8-dev")

    puts(green('-> Installing libpng12-dev'))
    cuisine.package_ensure("libpng12-dev")

    puts(green('-> Installing htop'))
    cuisine.package_ensure("htop")

    puts(green('-> Installing iftop'))
    cuisine.package_ensure("iftop")

    
##
## Config 
##
def config():
    """ Config recipe """

    if not cuisine.user_check(DEFAULT_USER):

        puts(green('-> Creating default user: %s' % DEFAULT_USER))
        cuisine.user_create(DEFAULT_USER)
        password = getpass.getpass('Enter your password: ')
        cuisine.user_passwd(DEFAULT_USER, password, encrypted_passwd=False)

        puts(green('-> Adding user to sudo'))
        cuisine.group_user_add('sudo', DEFAULT_USER)

        puts(green('-> Creating tmux config'))
        cuisine.file_upload('/home/%s/.tmux.conf' % DEFAULT_USER, 
                './provision/recipes/setup/tmux.conf',
                sudo=DEFAULT_USER)

        puts(green('-> Config SSH')) 
        cuisine.sudo('sed -i "s/PermitRootLogin yes/PermitRootLogin no/g" /etc/ssh/sshd_config')
        cuisine.sudo('sed -i "s/LoginGraceTime 120/LoginGraceTime 30/g" /etc/ssh/sshd_config')
        cuisine.sudo('echo "AllowUsers nekro" >> /etc/ssh/sshd_config')

    if cuisine.user_check('vagrant'):
        puts(green('-> Creating tmux config'))        
        cuisine.file_upload('/home/vagrant/.tmux.conf', 
                './provision/recipes/setup/tmux.conf',
                sudo='vagrant')

        puts(green('-> Config SSH for vagrant')) 
        cuisine.sudo('sed -i "s/AllowUsers nekro/AllowUsers nekro vagrant/g" /etc/ssh/sshd_config')

    puts(green('-> Restart SSHD')) 
    cuisine.sudo('/etc/init.d/ssh restart')
    
