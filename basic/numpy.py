
# NumPy (Numerical Python) pip3 install numpy
import numpy as np
# Create list baseball

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball=np.array(baseball)
print(np_baseball)

x = [4 , 9 , 6, 3, 1]
x[1]
y = np.array(x)
y[1]

##### Calculate the BMI: bmi
#np_height_m = np.array(height_in) * 0.0254
#np_weight_kg = np.array(weight_lb) * 0.453592
#bmi = np_weight_kg / np_height_m ** 2

# Create the light array
#light=np.array(bmi>21)
#print(light)  // [ True  True  True ...  True  True  True]
# Print out BMIs of all baseball players whose BMI is below 21
#print(bmi[light])



##### 2D NUMPY ARRAY   ######

# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]
updated = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball=np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball)) # numpy.ndarray
print(np_baseball) #[[180.   78.4]
                   # [215.  102.7]
                   # [210.   98.5]
                   # [188.   75.2]]

# Print out the shape of np_baseball
print(np_baseball.shape) #(4, 2)

# Print out the 50th row of np_baseball
print(np_baseball[49,:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb=np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[123,0])

# Print out addition of np_baseball and updated

print(np_baseball+ updated)
# Create numpy array: conversion
conversion=np.array([0.0254,0.453592,1.])

# Print out product of np_baseball and conversion
print(np_baseball*conversion)


#######BASIC STATISTIC ##########

# mean() => it is used to total sum of the values (or observations) divided by the number of values.
# median() => The median of a sample of numeric data is the value that lies in the middle when we sort the data. 
#corrcoef() =>
# std() => 
# sum() =>
# sort() =>

# Create np_height_in from np_baseball
np_height_in=np_baseball[:,0]

# Print out the mean of np_height_in (ortalama)
print(np.mean(np_height_in))

# Print out the median of np_height_in(tam ortadaki deger)
print(np.median(np_height_in))