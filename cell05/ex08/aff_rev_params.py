#!/usr/bin/python3

import sys

try :
    if len(sys.argv) >= 3:
        n = len(sys.argv)
        while n != 1 :
            print(sys.argv[n-1])
            n = n - 1
    else :
        print("none")
except :
	print("\nError")