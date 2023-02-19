# Question 1. Write a function to print "hello_USERNAME!" USERNAME is the input of the function.

def hello_username(user_name):
    """Print simple greeting hello_USERNAME"""
    print("Hello, " + user_name.upper() + "!")

name = input("Please enter a username. " )
hello_username(name)

# Question 2. Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.

def first_odds():
    for num in range (1, 100):
        if num % 2 != 0:

            return num


