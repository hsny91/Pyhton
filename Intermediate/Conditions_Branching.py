####
# equal: ==
#not equal: !=
#greater than: >
#less than: <
#greater than or equal to: >=
#less than or equal to: <=

# If statement example
age = 19
#age = 18
#expression that can be true or false
if age > 18:
    #within an indent, we have the expression that is run if the condition is true
    print("you can enter" )
#The statements after the if statement will run regardless if the condition is true or false 
print("move on")

# Elif statment example

new_age = 18
if new_age > 18:
    print("you can enter" )
elif new_age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    
print("move on")

####### Logical Operators #######
## AND, OR, NOT

# Condition statement example

album_year = 1990

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")
