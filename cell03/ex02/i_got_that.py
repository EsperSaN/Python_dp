#!/usr/bin/python3

try :
    str = input("What you gotta say? : ")
    while 1 : 
        str= input("I got that! Anything else? : \n") 
        if str == "STOP" : break 
except :
	print("\nEXIT")