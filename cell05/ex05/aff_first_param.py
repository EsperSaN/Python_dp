#!/usr/bin/python3

import sys

try :
	if len(sys.argv) >= 2:
		print(sys.argv[1])
	else:
		print("none")
except :
	print("\nError")