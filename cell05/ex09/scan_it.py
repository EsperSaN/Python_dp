#!/usr/bin/python3

import sys
import re as r
try	:
    if len(sys.argv) == 3:
        print(len(r.findall(sys.argv[1], sys.argv[2])))
    else:
       print("none")
except :
	print("\nError")
 