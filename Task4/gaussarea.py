#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
from scipy.integrate import quad

def gauss(x, A, x0, sigma, z0):
    return (A * np.exp((-((x-x0)**2)) / (2 * (sigma**2))) + z0)

# I tried to make "A" as name for the variable, but it would consider it any constant and not a variable.
# That is the reason I changed the name to avar, from a variable.
# Getting the input from user
avar = eval(input("Enter a value for the amplitude: "))  
x0 = eval(input("Enter a value for the peak center: "))
sigma = eval(input("Enter a value for the width: "))
z0 = eval(input("Enter a value for the offset: "))
a = eval(input("Enter a value for the lower integration limit: "))
b = eval(input("Enter a value for the upper integration limit: "))

# Creating the Gaussian curve and finding the area between the two limits
x = np.linspace(-10, 10, 200) 
y = gauss(x, avar, x0, sigma, z0)
area, error = quad(gauss, a, b, args=(avar, x0, sigma, z0))
print(f"The value for the integral between 0 & 2.5: {area:.2f}")

# Plotting the Gaussian curve
plt.plot(x, y, 'g-', label='Gaussian function')

# Filling the integration area
x_fill = np.linspace(a, b, 100)
y_fill = gauss(x_fill, avar, x0, sigma, z0)
plt.fill_between(x_fill, y_fill, alpha=0.3, color='steelblue', 
                 label=f'Area = {area:.2f}')

# The integration limits (vertical lines)
plt.axvline(a, color='seagreen', linestyle='--', alpha=0.7, label=f'x={a}')
plt.axvline(b, color='seagreen', linestyle='--', alpha=0.7, label=f'x={b}')

# Formatting
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gaussian function')
plt.legend()
plt.xlim(-10, 10)
plt.show()


# In[ ]:




