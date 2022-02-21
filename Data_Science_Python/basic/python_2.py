########### DATA SCIENCE TOOLBOX ############
# https://www.kaggle.com/kanncaa1/data-sciencetutorial-for-beginners
#USER DEFINED FUNCTION
def tuple_ex():
    """ return defined t tuple"""
    t = (1,2,3)
    return t
a,b,c = tuple_ex()
print(a,b,c)


##SCOPE
# global: defined main body in script
# local: defined in a function
# built in scope: names in predefined built in scope module such as print, len


x = 2  ##global scope
def f():
    x = 3  ##local scope
    return x
print(x)      # x = 2 global scope
print(f())    # x = 3 local scope

##NESTED FUNCTION

#nested function
def square():
    """ return square of value """
    def add():
        """ add two local variable """
        x = 2
        y = 3
        z = x + y
        return z
    return add()**2
print(square())  

#DEFAULT and FLEXIBLE ARGUMENTS
##  Default argument example def f(a, b=1)   """ b = 1 is default argument"""
# Flexible argument example: def f(*args):   """ *args can be one or more"""
# def f(** kwargs)  """ **kwargs is a dictionary"""

# default arguments
def f(a, b = 1, c = 2):
    y = a + b + c
    return y
print(f(5))
# what if we want to change default arguments
print(f(5,4,3))

# flexible arguments *args
def f(*args):
    for i in args:
        print(i)
f(1)
print("")
f(1,2,3,4)


def f(**kwargs):
    """ print key and value of dictionary"""
    for key, value in kwargs.items():           
        print(key, " ", value)
f(country = 'spain', capital = 'madrid', population = 123456)


# LAMBDA FUNCTION
# lambda function
square = lambda x: x**2     # where x is name of argument
print(square(4))
tot = lambda x,y,z: x+y+z   # where x,y,z are names of arguments
print(tot(1,2,3))

#ANONYMOUS FUNCTİON

number_list = [1,2,3]
y = map(lambda x:x**2,number_list)
print(list(y))


####  ITERATORS ###
# iterable: an object with an associated iter() method example: list, strings and dictionaries
# iterator: produces next value with next() method

# iteration example
name = "ronaldo"
it = iter(name)
print(next(it))    # print next iteration
print(*it)

# zip example
list1 = [1,2,3,4]
list2 = [5,6,7,8]
z = zip(list1,list2)
print(z)
z_list = list(z)
print(z_list) ## [(1, 5), (2, 6), (3, 7), (4, 8)]

un_zip = zip(*z_list)
un_list1,un_list2 = list(un_zip) # unzip returns tuple
print(un_list1) #(1, 2, 3, 4)
print(un_list2) # (5, 6, 7, 8)
print(type(un_list2))

###LIST COMPREHENSİON #####

num1 = [1,2,3]
num2 = [i + 1 for i in num1 ]
print(num2) # [2, 3, 4]

# Conditionals on iterable
num1 = [5,10,15]
num2 = [i**2 if i == 10 else i-5 if i < 7 else i+5 for i in num1]
print(num2) # [0, 100, 20]