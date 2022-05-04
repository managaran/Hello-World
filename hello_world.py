print("Hello World")

name = "Marlon"
print("Hello" , name)	# with a comma
print("Hello " + name)	# with a +

name = 68
print("Hello", name, "!")	# with a comma
print("Hello " + str(name) + "!")	# with a +	-- this one should give us an error!

fave_food1 = "spicy ahi poke"
fave_food2 = "loco moco"
print("I love to eat {} and {}." .format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string

name = "Marlon"
kids = 2
print("My name is %s and I have %d kids." % (name, kids))

x = "cheehoo"
print(x.upper())