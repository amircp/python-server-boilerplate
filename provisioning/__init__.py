# -*- coding: utf-8 -*-

"""
    Provisioning script
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

import cuisine
from fabric.colors import red, green
from fabric.utils import puts

# Import recipes here

def configure_host(devel=False):
    puts(green('-- Provisioning '))    
    puts(green('### Start host configurations  ###'))

    # Call recipes here

    if devel:
        puts(green('### Configurating options only for development environments ###'))

        # Call recipes only for development here

