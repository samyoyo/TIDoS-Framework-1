#!/usr/bin/env python2
# coding: utf-8

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#This module requires TIDoS Framework
#https://github.com/the-Infected-Drake/TIDoS-Framework 

import sys
import os
import time
import subprocess
import random
from vulnban1 import *
from random import randint
from subprocess import call
sys.path.append('modules/AuxilMods/')

from encodeall import *
from brutemods import *

def auxil(web):

    print ''
    time.sleep(0.3)
    print W+'\n [*] Type Selected : Auxillaries...\n'
    auxilban()
    v = raw_input (''+GR+'  [#] \033[1;4mTID\033[0m'+GR+' :> ' + color.END)
    print ''
    if v == '1':
	print ' [!] Type Selected : Bruteforce Modules'
	brutemods(web)
	print '\n\n'
	vulnban1()
	vuln(web)

    elif v == '2':
	print ' [!] Type Selected : Encode Strings'
	encodeall()
	print '\n\n'
	vulnban1()
	vuln(web)

    elif v == '99':
	print GR+' [*] Going back!'
	vulnban1()
	vuln(web)
	time.sleep(0.6)

