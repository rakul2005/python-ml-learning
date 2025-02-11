#📅 Day 2: Python Data Structures (Lists, #Tuples, Sets, and Dictionaries)

#🔹 Topics for Today
#Today, we’ll dive into Python’s data #structures—fundamental for handling data in #Machine Learning & AI.

#✅ Lists (Dynamic arrays)
#✅ Tuples (Immutable sequences)
#✅ Sets (Unique unordered collections)
#✅ Dictionaries (Key-value pairs)

#lists - ordered & mutable 

#creating a list
fruits = ["apple","banana", "cherry"]
print(fruits)

#modifying elements
fruits[1] = "blueberry"
print(fruits)

#adding elements 
fruits.append("orange")
fruits.insert(1, "grape")
print(fruits)

#removing elements
fruits.remove("apple")
popped_item = fruits.pop()
print(fruits, "| removed:", popped_item)

#list slicing
print(fruits[:1])

# tuples - ordered & immutable 

# creating a tuple
coordinates = (20.4, 45.8, 70)
print(coordinates)

# accessing elements
print(coordinates[2])

# tuple unpacking 
x, y, z = coordinates
print(f"x: {x}, y: {y}, z: {z}")

# a tuple can't be modified like lists

# sets - unordered and unique values 
# creating sets 

unique_numbers = {1,2,2,3,4,4,5} # duplicates gets removed since sets won't support duplicates
print(unique_numbers)

# adding and removing elements
unique_numbers.add(6)
unique_numbers.remove(3)
print(unique_numbers)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))     # {1, 2, 3, 4, 5}
print(set1.intersection(set2))      # {3}
print(set1.difference(set2))        # {1, 2}

# 4. dictionaries key value pairs

# creating a dictionary
student = {"name": "Alice", "age": 22, "course": "AI"}
print(student)

# accessing values
print(student["course"])

# adding and modifying data
student["age"] = 23
student["city"] = "Boston"
print(student)

# removing a key-value pair
del student["age"]
print(student)

# iterating through dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# practice problems 

# Lists Practice
# Create a list of five numbers
numbers = [3, 5.6, 11.2, 60.3]
print(numbers)

# Modify the third element
numbers[3] = 129.4
print(numbers)

#Remove the first element
numbers.remove(3)
print(numbers)

#Print the sum of the list
total = sum(numbers)
print("sum of the list:", total)

# 2. Tuples Practice
# Create a tuple of three favorite books/movies

movies = ("interstellar", "fast and furious", "oppenheimer")
print(movies)

#Try to change an element (observe the error)
# make a list out of the tuple and then modify back as a tuple

movies = ("interstellar", "fast and furious", "oppenheimer")
temp_list = list(movies)
temp_list[1] = "minions"
movies = tuple(temp_list)

print(movies)

# 3. Sets Practice

# Create a set of random numbers (some duplicates).
num = {1,2,3,4,5,5,6,7,8,8,9}
print(num)

# add numbers to the set num
num.add(10)
num.remove(1)
print(num)

#Find the union and intersection of two sets.
set3 = {3,4,5,7}
set4 = {13,14,17,19}

print(set3.union(set4))
print(set3.intersection(set4))
print(set4.difference(set3))





