#!/usr/bin/python3

try :
    num = int(input("Please tell me your age: "))
    if num < 0 : 
        print("Is that time travel???!! you are not born yet.")
    else :
        print(f"You are currently {num} years old.")
        print(f"In 10 years, you will be {num + 10} years old.")
        print(f"In 20 years, you will be {num + 20} years old.")
        print(f"In 30 years, you will be {num + 30} years old.")
except ValueError:
	print("ERROR : please enter the correct input.")
except :
	print("\nEXIT")