#!/usr/bin/python3

try :
	password = "Python is awesome"
	input = input()
	if input == password: print("ACCESS GRANTED")
	else: print("ACCESS DENIED")
except :
	print("ERROR")
