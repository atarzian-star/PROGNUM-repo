#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 3.22

import numpy as np
import matplotlib.pyplot as plt

x = range(-5, 6, 1)
y = np.cosh(x)
print(y)

x_np = np.arange(-5, 6, 1)
y_np = np.cosh(x_np)
print(y_np)

#Customizing the plot and showing it
plt.plot(x, y, marker='o', color='green', label="Cosh of x") 
plt.xlabel('x values', fontsize = 14)
plt.ylabel('y values', fontsize = 14)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.axis([-6, 6, 0, 80])
plt.title('Plot of cosh')
plt.grid(True)
plt.legend(fontsize = 14)
plt.show()

