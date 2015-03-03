# -*- coding: ISO-8859-1 -*-
#
# $Id: build_CL1356T_SDK_C_Doc_msi.py 2991 2010-04-30 14:03:23Z pvergain $

from __future__ import print_function

import subprocess
from subprocess import Popen as subprocess_Popen

def os_system(command):
    """Execute a command"""
    proc = subprocess_Popen(command, shell=True,stdout=subprocess.PIPE,)
    stdout_value = proc.communicate()[0]
    #_logger.info(stdout_value)
      
def build_msi(wsiname = 'CL1356T_SDK_C_Doc_Installer.wsi',msiname='CL1356T_SDK_C_Doc_Installer.msi'):
    cmd = 'WFWI.EXE %s /c /o "%s" /s' % (wsiname, msiname)
    os_system(cmd)
    #_logger.info('Building of %s successfull' % app.msiname)
    
build_msi()

print ("OK build_msi")


