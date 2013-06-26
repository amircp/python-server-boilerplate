# -*- coding: utf-8 -*-

"""
    Provisioning and deploy in remote servers
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

import cuisine
from provision.enviroments import development, staging, production
from provision import settings

# Import recipes here
from provision.recipes import main, python, nginx, uwsgi, postgres, gitolite


##
## Commands for remote hosts 
##

def setup_host():
    """ Configure host with recipes """

    ## Install basic packages 
    main.install()

    # Call recipeshere
    # Comment/uncomment examples

    python.install()
    nginx.install()
    uwsgi.install()
    postgres.install()


def install_git_server():
    """ Install and config gitolite """
    gitolite.install()
