#!/usr/bin/python3

import sys

def downcase_it(string) :
	return (string.lower())

if __name__ == "__main__":
    try :
        if len(sys.argv) >= 2:
            for av in range(1, len(sys.argv)):
                print(downcase_it(sys.argv[av]))
        else:
            print("none")
    except:
        print("\nError")
else :
    print("downcase_all.py cant imported as module .")
