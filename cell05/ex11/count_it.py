#!/usr/bin/python3

import sys

try :
	if len(sys.argv) >= 2:
		print(f"parameters: {len(sys.argv) - 1}$")
		for av in range(1, len(sys.argv)) : print(f"{sys.argv[av]}: {len(sys.argv[av])}")
	else:
		print("none")
except :
	print("\nError")