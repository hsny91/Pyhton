import numpy as np 
import matplotlib.pyplot as plt


# Makeup a numpy array within [-2, 2] and 5 elements
print(np.linspace(-2, 2, num=5)) # [-2. -1.  0.  1.  2.]

# Make a numpy array within [0, 2π] and 100 elements 
x = np.linspace(0, 2*np.pi, num=100)
y = np.sin(x)

# Plot the result
plt.plot(x, y)