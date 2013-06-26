# -*- coding: utf-8 -*-

"""
    Setup recipe
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

import cuisine
from fabric.colors import red, green
from fabric.utils import puts


DEFAULT_USER = 'nekro'


##
## Install packages 
##
def install(username, password, public_key):
    """ Install packages """

    if not cuisine.user_check(username):

        puts(green('-> Creating default user: %s' % username))
        cuisine.user_create(username, shell='/bin/bash')
        cuisine.user_passwd(username, password, encrypted_passwd=False)
        
        if public_key != '':
            puts(green('-> Uploading public key'))    
            cuisine.file_upload('~/.ssh/authorized_keys', public_key)

        puts(green('-> Adding user to sudo'))
        cuisine.group_user_add('sudo', username)

        puts(green('-> Creating tmux config'))
        cuisine.file_upload('/home/%s/.tmux.conf' % username, 
                './provision/config/tmux.conf',
                sudo=username)

        puts(green('-> Config SSH')) 
        cuisine.sudo('sed -i "s/PermitRootLogin yes/PermitRootLogin no/g" /etc/ssh/sshd_config')
        cuisine.sudo('sed -i "s/LoginGraceTime 120/LoginGraceTime 30/g" /etc/ssh/sshd_config')
        cuisine.sudo('echo "AllowUsers %s" >> /etc/ssh/sshd_config' % username)

    if cuisine.user_check('vagrant') and not cuisine.file_exists('/home/vagrant/.tmux.conf'):
        puts(green('-> Creating tmux config'))        
        cuisine.file_upload('/home/vagrant/.tmux.conf', 
                './provision/config/tmux.conf',
                sudo='vagrant')

        puts(green('-> Config SSH for vagrant')) 
        cuisine.sudo('sed -i "s/AllowUsers {0}/AllowUsers {0} vagrant/g" /etc/ssh/sshd_config'.format(username))

    puts(green('-> Restart SSHD')) 
    cuisine.sudo('/etc/init.d/ssh restart')

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

    
