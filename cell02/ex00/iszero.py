#!/usr/bin/python3

try :
	num = float(input())
	if num == 0 : print("This number is equal to zero.")
	else : print("This number is different from zero.")
except ValueError:
	print("Only numbers are allowed THX YOU for Understanding.")
except :
	print("\nEXIT")