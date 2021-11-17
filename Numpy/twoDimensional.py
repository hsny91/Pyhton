import numpy as np 
import matplotlib.pyplot as plt

# Create a list
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
print(a)

# Convert list to Numpy Array
# Every element is the same type
A = np.array(a)
print(A)  ##[[11 12 13]
          ##[21 22 23]
          ##[31 32 33]]

# Show the numpy array dimensions
print(A.ndim) # 2

# Show the numpy array shape
print(A.shape) # (3, 3)

# Show the numpy array size
print(A.size) #9 

# Access the element on the second row and third column
print(A[1, 2]) #23

# Access the element on the second row and third column
print(A[1][2]) #23

# Access the element on the first row and first and second columns
print(A[0][0:2])  # [11 12]

##### Basic Operations ######

# Create a numpy array X and Y
X = np.array([[1, 0], [0, 1]]) 
Y = np.array([[2, 1], [1, 2]]) 
# Add X and Y
Z = X + Y
print(Z)  ##[[3 1]
          ##[1 3]]

# Multiply Y with 2
M = 2 * Y
print(M) # array([[4, 2],[2, 4]])

# Multiply X with Y
N = X * Y
print(N) # array([[2, 0],0, 2]])

# Create a matrix S and H
H = np.array([[0, 1, 1], [1, 0, 1]])
S = np.array([[1, 1], [1, 1], [-1, 1]])

# Calculate the dot product
R = np.dot(H,S)
print(R) # [[0 2][0 2]]