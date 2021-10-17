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

# Check the type of the values stored in numpy array
print(nummpy_a.dtype) # int64
 
# Create a numpy array
b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])

# Check the type of array
print(type(b)) #numpy.ndarray

# Check the value type
print(b.dtype) #dtype('float64')

##### INDEX SLICING #####

# Create numpy array
c = np.array([20, 1, 2, 3, 4])

# Assign the first element to 100
c[0] = 100
print(c) # [100   1   2   3   4]

# Slicing the numpy array
d = c[1:4]
print(d) # array([1, 2, 3])

# Set the fourth element and fifth element to 300 and 400
c[3:5] = 300, 400
print(c) #[100   1   2 300 400]