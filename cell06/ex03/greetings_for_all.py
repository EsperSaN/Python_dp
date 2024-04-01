#!/usr/bin/python3

def greetings(string = "noble stranger") :
    if type(string) != str: return print("Error! It was not a name.")
    print("Hello, " + string + ".")


greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)