# An exception is an error that occurs during the execution of code. 
# This error causes the code to raise an exception and if not prepared to handle it will halt the execution of the code.
# ZeroDivisionError, NameError, IndexError 


# Try Except Example
a = 1
try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except:
    print("There was an error")


c = 1

try:
    b = int(input("Please enter a number to divide a"))
    c = c/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success c=",c)    