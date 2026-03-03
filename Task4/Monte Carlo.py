#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 4.6

import numpy as np
from numpy import sin, cos, tan, log, log10

# Asking for user input for the funtion and boundaries
function = input("Enter a function f(x) = ")
a = eval(input("Enter a value for the lower boundary: "))
b = eval(input("Enter a value for the upper boundary: "))
N = 1000000

# Calculating the final value using Monte Carlo
x = np.random.uniform(a, b, N) 
y = eval(function)
value = ((b-a) / N) * sum(y)

# Printing the value to check it is ok
print(value)

