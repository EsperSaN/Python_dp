#!/usr/bin/python3
import math
try :
    num = float(input("Give me a number: "))
    print(f"{math.ceil(num)}")
except ValueError:
	print("Only numbers are allowed THX YOU for Understanding.")
except :
	print("\nEXIT")