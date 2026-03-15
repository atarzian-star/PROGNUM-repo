#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 3.1

# in the order of 
# ‘Sun’, ‘Jupiter’, ‘Saturn’, ‘Neptune’, ‘Uranus’, ‘Earth’, ‘Venus’, ‘Mars’, ‘Mercury’, ‘Moon’, ‘Pluto’

masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]

# Making the new list
new_masses = []

for i in range(len(masses)):
    if 7.349e+22 < masses[i]:
        new_masses.append(masses[i])
        
print(new_masses)
print()
        
# Slicing the list    
m_slice = masses[6::]
print(m_slice)
print()
    
# Finding the average value of the slice
a = sum(m_slice) / len(m_slice)
print(a)

