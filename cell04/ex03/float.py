#!/usr/bin/python3

try :
    num = float(input("Give me a number: "))
    num = num % 1
    if num == 0 : print("This number is an integer.")
    else : print("This number is a decimal.")
except ValueError:
	print("Only numbers are allowed THX YOU for Understanding.")
except :
	print("\nEXIT")