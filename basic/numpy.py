
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