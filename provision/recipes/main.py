# -*- coding: utf-8 -*-

"""
    Main recipe
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

import cuisine
from fabric.colors import green
from fabric.utils import puts

##
## Install packages 
##
def install():
    """ Install main packages """

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

    puts(green('-> Installing git'))
    cuisine.package_ensure("git")


##
## Main setup
##
def setup():
    """ Main setup"""

    puts(green('-> Configuring SSHD')) 
    cuisine.sudo('sed -i "s/LoginGraceTime 120/LoginGraceTime 30/g" /etc/ssh/sshd_config') 
    puts(green('-> Restart SSHD')) 
    cuisine.sudo('/etc/init.d/ssh restart')

    if cuisine.user_check('vagrant') and not cuisine.file_exists('/home/vagrant/.tmux.conf'):
        puts(green('-> Creating tmux config'))        
        cuisine.file_upload('/home/vagrant/.tmux.conf', 
                './provision/config/tmux.conf',
                sudo='vagrant')
