try :
	name = input("Hey, what's your first name? : ")
	last_name = input("And your last name? : ")
	last_name = last_name.strip()
	name = name.strip()
	print("Well, pleased to meet you, " + name + " "+ last_name + ".")
except :
	print("\nERROR")