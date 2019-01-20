# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 21:02:28 2017

@author: HaiyanJiang
"""

'''
##this does not work
'''


import pip
from subprocess import call

for dist in pip.get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)

pack = pip.get_installed_distributions()
len(pack)
pack[3]
pack[3].project_name
#

for dist in pack:
    print(dist.project_name)


###############################################
# if succeeded, return 0; if failed, return 2
call("pip list") # returns 0
call("pip install --upgrade sklearn", shell=False) # returns 2, failed
call("pip install --user --upgrade sklearn", shell=False) # returns 0, succeeded








