#!/usr/bin/python3

import sys

try	:
    if len(sys.argv) == 2:
        if (input("What was the parameter? ") == sys.argv[1]):
            print("Good job!")
        else:
            print("Nope, sorry...")
    else:
        print("none")
except :
	print("\nError")