#!/usr/bin/python3

try :
    num = int(input("Give me the first number: "))
    num2 = int(input("Give me the second number: "))
    print("Thank you!")
    print(f"{num} + {num2} = {num + num2}\n{num} - {num2} = {num - num2}\n{num} / {num2} = {num / num2}\n{num} * {num2} = {num * num2}")
except ValueError :
	print("Only numbers are allowed THX YOU for Understanding.")
except :
	print("\nEXIT")