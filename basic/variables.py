#int, or integer: a number without a fractional part. savings, with the value 100, is an example of an integer.
#float, or floating point: a number that has both an integer and fractional part, separated by a point. 
#str, or string: a type to represent text. You can use single or double quotes to build a string.
#bool, or boolean: a type to represent logical values. Can only be True or False (the capitalization is important!
#you can find type of variables with type(name)



#Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
x = y = z = "Orange" 

print(x) # Orange
print(y) # Orange
print(z) # Orange

fruits = ["apple", "banana", "banana"]
x, y, z = fruits

print(x) #apple
print(y) #banana
print(z) #banana

#If you try to combine a string and a number, Python will give you an error:
x = 5
y = "John"
#print(x + y) # error


savings = 100
growth_multiplier = 1.1
result = 100 * 1.10 ** 7
desc = "compound interest"
print(type(savings))  #int
print(type(growth_multiplier)) # float

# Assign product of growth_multiplier and savings to year1
year1=savings*growth_multiplier

# Print the type of year1
print(type(year1))

# Assign sum of desc and desc to doubledesc

doubledesc=desc+desc

# Print out doubledesc(i expect compound interestcompound interest)
print(doubledesc) 

######  DATA TYPE #########

#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview

x = "Hello World"	#str	
x = 20	#int	
x = 20.5	#float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview


####   CONVERT TO TYPE   ######

#int(), float() and bool() will help you convert Python values into any type.
# str()to convert a value into a string

print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")
# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float=float(pi_string)



###### Python Casting ########
