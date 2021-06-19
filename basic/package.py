import math

print('pi is', math.pi)

# Definition of radius
r = 0.43

# Import the math package
import math

# Calculate C
C = 2*(math.pi)*r

# Calculate A
A = math.pi*r**2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

# Definition of radius
r = 192500

##### IMPORT JUST ONE MATH FUNCTION ###

# Import radians function of math package
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
dist=r*radians(12)

# Print out dist
print(dist)

# Suppose you want to use the function inv(), which is in the linalg subpackage of the scipy package. You want to be able to use this function as follows:

# from scipy.linalg import inv as my_inv #