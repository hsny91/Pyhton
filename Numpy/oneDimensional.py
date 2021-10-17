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

####### BASIC OPERATION #########
# Create a numpy array
new_array= np.array([0, 1, 2, 3, 4])
print(new_array)

# Get the size of numpy array
print(new_array.size) # 5

# Get the number of dimensions of numpy array
print(new_array.ndim) # 1

# Get the shape/size of numpy array
print(new_array.shape) # (5,)

# Get the biggest value in the numpy array
max_value=new_array.max()
print(max_value) # 4

# Get the smallest value in the numpy array
min_value = new_array.min()
print(min_value) # 0

###### Numpy Array Operations ######

u = np.array([1, 0])
v = np.array([0, 1])

# Numpy Array Addition
z = u + v
print(z) #  [1 1]

# Numpy Array Multiplication
multi_array = 2 * z
print(multi_array) # [2 2]

###### Product of Two Numpy Arrays ######

# Create a numpy array
first_array = np.array([1, 2])
second_array= np.array([3, 2])

# Calculate the production of two numpy arrays
third_array = first_array*second_array
print(third_array) #  [3 4]

# Calculate the dot product
print(np.dot(first_array, second_array)) # 7

# Add the constant to array
print(third_array+1) # [4 5]

# Get the mean of numpy array(avarage)
mean = third_array.mean()
print(mean) #  3.5

##### Mathematical Functions #### 

# The value of pi
print(np.pi) #  3.14159265359

# Create the numpy array in radians
k = np.array([0, np.pi/2 , np.pi])

# Calculate the sin of each elements
l = np.sin(k)
print(l) # [  0.00000000e+00   1.00000000e+00   1.22464680e-16]