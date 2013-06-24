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
        

##
## Config 
##
def config():
    """ Config recipe """
    
    puts(green('-> Creating git user'))
    cuisine.user_ensure('git')
