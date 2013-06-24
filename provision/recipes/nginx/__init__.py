# -*- coding: utf-8 -*-

"""
    Nginx recipe
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
    puts(green('-> Installing nginx'))
    cuisine.package_ensure('nginx')
        

##
## Config 
##
def config():
    """ Config recipe """
    pass
