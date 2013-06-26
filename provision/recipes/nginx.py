# -*- coding: utf-8 -*-

"""
    Nginx recipe
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

import cuisine
from fabric.colors import green
from fabric.utils import puts


##
## Install packages 
##
def install():
    """ Install ngix packages """

    puts(green('-> Installing nginx'))
    cuisine.package_ensure('nginx')

    puts(green('-> Creating apps user'))
    cuisine.user_ensure('apps')
   
    puts(green('-> Creating dirs for web apps'))
    cuisine.dir_ensure('/home/apps/www')
    cuisine.dir_ensure('/home/apps/logs')
