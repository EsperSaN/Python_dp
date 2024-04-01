#!/usr/bin/python3

try :
    num = float(input())
    if num == 0 : 
        print("This number is both positive and negative.")
    if num < 0 : 
        print("This number is negative.")
    if num > 0 : 
        print("This number is positive.")
except ValueError:
	print("Only numbers are allowed THX YOU for Understanding.")
except :
	print("\nEXIT")