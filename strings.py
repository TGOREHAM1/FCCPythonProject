print("New \n Line")

my_string = "ALL UPPER CASE STRING"

print("Look at this " + my_string + " that I created." + "\nSee it's " + str(my_string.isupper()))
print(my_string.index("A"))

my_string = my_string.lower()
print("Look, I made my '" + my_string.lower() + "' a liar.\nSee, it's now " + str(my_string.isupper()))

print(my_string.index("a"))

print(my_string.replace("upper", "lower"))