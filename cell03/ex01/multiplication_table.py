#!/usr/bin/python3

try :
    num = int(input("Enter a number:\n"))
    loop = 0
    while loop < 10 :
        print(str(loop) + " x " + str(num) + " = " + str(num * (loop))) ; loop += 1
except ValueError:
	print("Error Please enter a valid Integer.")
except :
	print("\nEXIT")