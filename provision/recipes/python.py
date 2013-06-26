# -*- coding: utf-8 -*-

"""
    Python recipe
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

import cuisine
from fabric.colors import red, green
from fabric.utils import puts


##
## Install packages 
##
def install():
    """ Install python packages """

    puts(green('-> Installing python'))
    cuisine.package_ensure("python")
    
    puts(green('-> Installing python-dev'))
    cuisine.package_ensure("python-dev")

    puts(green('-> Installing python-pip'))
    cuisine.package_ensure("python-pip")

    puts(green('-> Install python virtualenv wrapper'))
    cuisine.sudo('pip install virtualenvwrapper')
