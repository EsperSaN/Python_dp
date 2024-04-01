#!/usr/bin/python3

import sys

try	:
    if len(sys.argv) == 3:
        st = int(sys.argv[1])
        end = int(sys.argv[2])
        ar = []
        for i in range(st, end + 1):
            ar.append(i)
        print(ar)
    else:
        print("none")
except ValueError:
    print("Please enter valid numbers")
except :
	print("Error")