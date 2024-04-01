#!/usr/bin/python3
try :
	num = int(input("Enter a number less than 25\n"))
	plus =  1
	if num > 25 : print("Error")
	else :
		while num <= 25 :
			print("Inside the loop, my variable is " + str(num)) ; num += plus
except ValueError:
	print("Error Please enter a NUMBER less than 25.")
except :
	print("\nEXIT")