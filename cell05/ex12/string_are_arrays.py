#!/usr/bin/python3

import sys as s

try :
    if len(s.argv) == 2:
        found = 0
        for n in s.argv[1]:
            if n == 'z' : print(n, end="") ; found = 1
        if found == 0: print("none")
        else : print()
    else :
        print("none")
except :
	print("\nError")