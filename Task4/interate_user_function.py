#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
from scipy.integrate import quad
# I tried to make f_eval with "from numpy import sin, cos, exp, pi", but I would get the error: 
# TypeError: unsupported operand type(s) for ** or pow(): 'numpy.ufunc' and 'float'
# And I've noticed that if instead I use np. for all expression it works well.
# I am not sure how to solve this with "from numpy import sin, cos, exp, pi", but I hope 
# my way of solving is ok and I would like to know how to fix this issue.


# Making the function that evaluates functions
def f_eval(expression, x):
    # Make x and expression available globally for eval
    global current_x, expression_global
    current_x = x
    expression_global = expression
    
    try:
        result = eval(expression_global)
        return result
    except NameError:
        print("Error: Unknown function. Use only np.sin(x), np.cos(x), np.exp(x), np.pi, x")
        print("Make sure to use x as the variable!")
        raise
    except SyntaxError:
        print("Error: Syntax wrong! Check for (), operators etc.")
        raise
    except:
        print("Error: Cannot evaluate expression! Try rewriting it again.")
        raise

# The main code
expression = input("Enter function f(x) [np.sin(x), np.cos(x), etc]: ")
a = eval(input("Enter lower limit a: "))
b = eval(input("Enter upper limit b: "))

# Using the Monte Carlo method to integrate
N = 100000
x_mc = np.random.uniform(a, b, N)
y_mc = np.zeros(N)

for i in range(N):
    y_mc[i] = f_eval(expression, x_mc[i])

area_mc = (b - a) * np.mean(y_mc)
print(f"Monte Carlo result: {area_mc:.2f}")

# Using the quad function method to integrate
def f_quad(x):
    return f_eval(expression, x)

area_quad, error_quad = quad(f_quad, a, b)
print(f"Quad result: {area_quad:.2f}")

