# Question 1. Write a function to print "hello_USERNAME!" USERNAME is the input of the function.

def hello_username(user_name):
    """Print simple greeting hello_USERNAME"""
    print("Hello, " + user_name.upper() + "!")

name = input("Please enter a username. " )
hello_username(name)

# Question 2. Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.

def first_odds():
    print("Odd numbers from 1-100 are: ")
    for x in range(1,100 +1, 2):
            print(x)
print(first_odds())

# Question 3. Please write a Python function, max_num_in_list to return the max number of a given list.

def max_num_in_list (a_list):
    max = a_list[0]
    
    for x in a_list:
        if x > max:
            max = x
    return max

a_list = [1, 19,55,65,89,302]
print("The largest number in the list is: " + str(max_num_in_list(a_list)) + ".")


# Question 4. Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    leap = False
    if a_year % 400 == 0:
        leap = True
    elif a_year % 4 == 0 and a_year % 100:
        leap = True
    return leap

year = int(input())
print(is_leap_year(year))

# Question 5. Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
# really stuck on this one!



