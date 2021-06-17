#int, or integer: a number without a fractional part. savings, with the value 100, is an example of an integer.
#float, or floating point: a number that has both an integer and fractional part, separated by a point. 
#str, or string: a type to represent text. You can use single or double quotes to build a string.
#bool, or boolean: a type to represent logical values. Can only be True or False (the capitalization is important!
#you can find type of variables with type(name)


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


####   CONVERT TO TYPE   ######

#int(), float() and bool() will help you convert Python values into any type.
# str()to convert a value into a string

print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")
# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float=float(pi_string)