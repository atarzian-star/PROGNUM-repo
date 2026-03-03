#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 4.3

import numpy as np

def who_wins(user, comp):

    if user == comp:
        return print("It's a tie! Try again! Maybe you will win.")
        
    if user == "R":
        if comp == "S":
            return print("You win! YAYAYAYAYAYAY")
        else:
            return print("You lose. Awh man :(")
        
    elif user == "P":
        if comp == "R":
            return print("You win! YAYAYAYAYAYAY")
        else:
            return print("You lose. Awh man :(")
        
    elif user == "S":
        if comp == "P":
            return print("You win! YAYAYAYAYAYAY")
        else:
            return print("You lose. Awh man :(")

# Starting the game
print("Let's play Rock Paper Scissors!!!")
print("Use R for Rock, P for Paper, S for Scissors.")
print()

user_choice = input("3! 2! 1! Choose now! (R/P/S)? ")

# Making the random computer choice
options = ["R", "P", "S"]
comp_choice = np.random.choice(options)

# Checking if the input is valid
if user_choice not in ["R", "P", "S"]:
    print("Nuh-uh, try again please! Type R, P, or S.")

else:
    a = who_wins(user_choice, comp_choice)

