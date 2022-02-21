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