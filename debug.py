# -*- coding:utf8 -*-
import sys

debug = True

def log(*args):
	if debug:
		for i in args:
			sys.stdout.write(str(i) + ' ')
		sys.stdout.write('\n') 
