#📅 Day 3: Functions & Modules in Python

#Goal: Understand how to create and use functions, arguments, return values, and modules to write reusable and structured code.
#🔹 Topics for Day 3

#✅ Functions
#✅ Function Arguments (Positional, Default, *args, **kwargs)
#✅ Return Statements
#✅ Lambda Functions

# 1. Creating Functions
#A function helps in structuring code, avoiding repetition, and improving readability.

def greet(name):
    return f"Hello {name}!"

print(greet("Alice"))
print(greet("Robert"))

# 2. Function Arguments
#You can pass positional arguments, default arguments, *args, and **kwargs to functions.

def introduce(name, age = 18):
    return f"My name is {name}, and I am {age} years old"

print(introduce("Bob", 25))
print(introduce("Charlie"))

# *args (Multiple Positional Arguments)

def add_numbers(*args):
    return sum(args) 

print(add_numbers(1,2,3,4))
print(add_numbers(3,4,5,7))

# **kwargs (Multiple Keyword Arguments)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name = "Alice", age = 22, city = "NY")

# 4. Lambda Functions (One-Line Functions)

double = lambda x: x * 2
print(double(300))

students = [("Alice", 85), ("Bob", 90), ("Charlie", 80)]
students.sort(key = lambda x: x[1])
print(students)

# 5. Importing & Using Modules
# Importing a Module

import math 
print(math.sqrt(16))

# Quick Practice Tasks
# Write a function that checks if a number is even or odd

def even_number(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
result = even_number(4)
print(result)

# Create a function that returns the factorial of a number

def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

print(factorial(10))

# Write a lambda function that returns the square of a number

square = lambda x: x**2
print(square(10))


def even_num(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_num(5))

def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

print(factorial(10))