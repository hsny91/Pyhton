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
print(1>0 and 4<5) #true

# Condition statement example

album_year = 1990

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")

###EXAMPLE###
liste=[1,2,3,4,5,6]
value= 6
if value in liste:
    print("yes {} value in the list".format(value))
else:
    print("no")

# 1640= 17.yy 109= 2.yy
# input year >1 and year<2005

def findCenturyYear(pYear):
    if pYear<1 or pYear>2005:
        print("please enter certain value")
    else:
        str_year=str(pYear)
        if(len(str_year)<3):
            return 1
        elif(len(str_year)==3):
            if(str_year[1:3]=="00"):
                return int(str_year[0])
            else:
                return int(str_year[0])+1
        else:
            if(str_year[2:4]=="00"):
                return int(str_year[:2])
            else:
                return int(str_year[:2])+1
print("century: ",findCenturyYear(99))
