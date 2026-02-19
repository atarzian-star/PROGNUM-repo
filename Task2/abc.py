#!/usr/bin/env python
# coding: utf-8

# In[7]:


from math import sqrt

# Asking for values from the user
a = eval(input("Enter the value of a: "))
b = eval(input("Enter the value of b: "))
c = eval(input("Enter the value of c: "))

# Checking if a is different than 0. If it is equal to 0,
# then it is not a quadratic equation and the algorithm won't work.
if a == 0:
    print("This is not a quadratic equation (a can't be 0).")
else:
    # Calculating the discriminant
    D = (b**2) - (4*a*c)

    # Checking the conditions
    if D > 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        print(f"The equation has two real solutions: x1 = {x1} and x2 = {x2}")

    elif D == 0:
        x = -b / (2*a)
        print(f"The equation has one real solution: x = {x}")

    else:
        print("The equation has no real solutions.")

