#A numpy array is similar to a list. 
# It's usually fixed in size and each element is of the same type.
# import numpy library
import numpy as np 

# Create a python list
a = ["0", 1, "two", "3", 4]

# Print each element
print("a[0]:", a[0]) # ('a[0]:', '0')
print("a[1]:", a[1]) # ('a[1]:', 1)
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

# Create a numpy array

nummpy_a = np.array([0, 1, 2, 3, 4])
print(nummpy_a) # [0 1 2 3 4]

# Check the type of the array
print(type(nummpy_a )) # numpy.ndarray
 