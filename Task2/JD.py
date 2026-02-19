#!/usr/bin/env python
# coding: utf-8

# In[4]:


print("All dates should be numbers.")
print()

# Asking for input from user
Y = eval(input("What is the year? "))
M = eval(input("What is the month? ")) 
D = eval(input("What is the day? ")) 

# Making the JD algorithm. I put // to have only the left part from the decimal point.
JD = 367*Y -7*(Y+(M+9)//12)//4 - 3*((Y+(M-9)//7)//100 + 1)//4 + (275*M)//9 + D + 1721029-0.5

print()
print("The number of days is:", JD)

