# -*- coding: utf-8 -*-

"""
    Uwsgi recipe
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
    puts(green('-> Installing uwsgi'))
    cuisine.package_ensure('uwsgi')
    cuisine.package_ensure('uwsgi-plugin-python')
        

##
## Config 
##
def config():
    """ Config recipe """
    pass

    
