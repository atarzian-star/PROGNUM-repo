#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Sirius data
# apparentMagnitude = -1.46
# absoluteMagnitude = 1.45

# The distance is related to the magnitudes as m-M=5.Log(d/10)
# 1 Parsec = 3.26164 ly

S1 = input("Enter the apparent magnitude for Sirius A: ")
m = float(S1)

S2 = input("Enter the absolute magnitude for Sirius A: ")
M = float(S2)

# m = apparentMagnitude
# M = absoluteMagnitude

d = 10.0 * pow( 10.0, (m - M)/5.0 ) * 3.26164

s = f"The distance to Sirius A is: {d}"
print(s)


# In[ ]:




