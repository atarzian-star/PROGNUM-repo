#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 6.14

class Fibonacci:
    """Class for calculating Fibonacci sequence"""
    def __init__(self):
        pass  # runs but does nothing, python requires a statement
    
    def nth(self, n):
        # Checking values are ok
        if n == 0:
            return "Umm are you sure n is 0?"
        elif n == 1:
            return 0
        
        a = 0
        b = 1
        
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        
        return c
    
    def div(self, n, m):
        # Checking values are ok
        if n == 0:
            return "Umm are you sure n is 0?"
        
        if m == 0:
            return "Silly you! You cant divide by 0!"
        
        # Making a list for the results and
        # setting the first two fibo numbers to be 0 and 1
        limit_n = self.nth(n)
        results = []
        
        a = 0
        b = 1
        c = 0
        
        # Creating a loop to find fibo numbers smaller than n
        # And checking if the number can be divided by m
        while c < limit_n:
            if c % m == 0:
                results.append(c)
                
            c = a + b
            a = b
            b = c
        
        return results

n = eval(input("What is the n? "))
m = eval(input("What is the m? "))

fib = Fibonacci()

# Testing the function
print(f"The {n} Fibonacci number is {fib.nth(n)}")
print(f"The numbers divisible by {m} from the fibo list until {fib.nth(n)} is")
print(fib.div(n, m))

