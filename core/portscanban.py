#!/usr/bin/env python2
# -*- coding : utf-8

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#This script is a part of TIDoS Framework
#https://github.com/the-Infected-Drake/TIDoS-Framework 

import time
import os
from time import sleep
from colors import *

def portscanban():

	print O+'\n     +--------------+'
	print O+'     |  '+W+'SCAN TYPES'+O+'  |'
	print O+'     +--------------+\n'
	sleep(0.1)
	print B+"     [1]"+C+" A Simple Port Scan"
	sleep(0.1)
	print B+"     [2]"+C+" A TCP Connect Scan"
	sleep(0.1)
#	print B+"     [3]"+C+" A TCP-ACK Scan"
#	sleep(0.1)
	print B+"     [4]"+C+" A TCP Stealth Scan"
	sleep(0.1)
#	print B+"     [5]"+C+" A UDP Scan"
#	sleep(0.1)
	print B+"     [6]"+C+" A XMAS Scan"
	sleep(0.1)
#	print B+"     [7]"+C+" A NULL Scan"
#	sleep(0.1)
	print B+"     [8]"+C+" A FIN Scan"
	sleep(0.1)
	print B+"     [9]"+C+" A Open Ports Services Detector"
	sleep(0.1)
#	print O+B+"   [10]"+C+" A TCP Windows Scan"
#	sleep(0.1)	
	print B+"     [A]"+C+" Automate all modules one by one\n"
	sleep(0.1)
	print B+'     [99]'+C+' Back\n'

