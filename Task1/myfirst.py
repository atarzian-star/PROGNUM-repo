#!/usr/bin/env python
# coding: utf-8

# Answers for Week 1
# 
# * Name: Anneliese Tarzian
# * Username: atarzian
# * Student s-number: S6199984
# * Group (AS1, etc.): AS1

# In[3]:


x = 22/7


# $$y=\frac{sin(x)}{x}$$

# In[1]:


pi = 22/7 # Processed on Jupyter Hub


# ![sillycat.png](attachment:sillycat.png)

# In[8]:


x = 1
x *= 2
x *= 3
x *= 4
x *= 5
x *= 6
print("x =",x)


# In[15]:


from scipy.constants import G
Mmoon = 7.342e22
Mearth = 5.9722e24
r = 385000600
F = (G * (Mmoon * Mearth)) / (r**2)
print("F =", F)


# In[12]:


from scipy.constants import G, pi
a = 149597870700
P = 31558150
M = ((4 * (pi**2)) * (a**3)) / (G * (P**2))
print("m1 + m2 =", M)


# In[13]:


x1 = 10
x2 = 22/7
print(x1, end="")
print(x2, end="")
#it prints out the values for x1 and x2 but without any space after them so they are on one line


# In[ ]:


#1.15
# a) it shows me the absolute path to the folder downloads (/Users/users/atarzian/Downloads)
# b) . refers to a shortcut to the current directory and
# .. refers to a shortcut to the parent directory 
# (the one right before, closer to the root of the directory tree/"one up")


# In[ ]:


#1.16
#cd ~/Desktop is the shortest command


# In[ ]:




