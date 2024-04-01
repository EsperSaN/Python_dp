#!/usr/bin/python3

try :
	num1 = int(input("Enter the first number:\n"))
	num2 = int(input("Enter the second number:\n"))
	result = num1 * num2
	print(str(num1) + " x " + str(num2) + " = " + str(result))
	if result == 0 : print("The result is positive and negative.")
	if result < 0 : print("The result is negative.")
	if result > 0 : print("The result is positive.")
except ValueError: 
    print("Error Please enter a valid Integer.")
except :
	print("\nEXIT")