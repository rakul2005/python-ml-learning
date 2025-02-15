#🎯 Day 4: Control Flow in Python
#Control flow structures allow us to control the execution of code based on conditions and loops.


# 1. Conditional Statements (if, elif, else)

age = 20

if age >= 18:
    print("You are an adult!")
elif age > 13:
    print("You are a teenager!")
else:
    print("You are a child!")

# 2. Loops in Python

for i in range(5):
    if i == 2:
        continue
    print(i)

# 3. List Comprehension (Python Magic 🪄)

numbers = [x for x in range(10) if x % 2 == 0]
print(numbers) # [0, 2, 4, 6, 8]

# 4. Enumerate and Zip (Pro Looping 🚀)
# enumerate(): Looping with an index 📍

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

for name, score in zip(names, scores):
    print(f"🏅 {name} scored {score}")

#🎯 📝 Fun Exercises for Practice

#1. Basic If-Else Challenge 🎭

num = 0

if num > 0:
    print("number is positive!")
elif num < 0:
    print("number is negative!")
else:
    print("number is equivalent to zero!")

#2. Loop exercises 🔄

#    Print all even numbers from 1 to 20 using a loop.

num = 0

for num in range(1,20):
    if num % 2 == 0:
        print(num, end= " ")

#    Sum all numbers from 1 to 100 using a for loop.

total = 0

for num in range(1,101):
    total += num

print(total)

# 3. FizzBuzz Game 🎮
#  Print numbers from 1 to 50.

# 1. standard approach (loop & conditionals) 
 
for number in range(1,11):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz 🎇")
    elif number % 3 == 0:
        print("Fizz 🍹")
    elif number % 5 == 0:
        print("Buzz 🐝")

# 2. list comprehension (one-liner fizzbuzz)

fizzbuzz_list = ["FizzBuzz 🎇" if num % 3 == 0 and num % 5 == 0 else
                 "Fizz 🍹" if num % 3 == 0 else
                 "Buzz 🐝" if num % 5 == 0 else
                 num
                 for num in range(1,51)
]

print("\n".join(map(str, fizzbuzz_list)))
      
# ⚡ 3. Generator Expression (Memory Efficient)

fizzbuzz_gen = (
    "FizzBuzz 🎇" if num % 3 == 0 and num % 5 == 0 else
    "Fizz 🍹" if num % 3 == 0 else
    "Buzz 🐝" if num % 5 == 0 else
    num
    for num in range(1,51)
)
print(*fizzbuzz_gen, sep="\n")  # Efficiently prints without storing all values in memory

# 4. Using a Dictionary for Better Readability

for num in range(1,51):
    output = {0: "Fizzbuzz 🎇", 3: "Fizz 🍹", 5: "Buzz 🐝"}.get(num % 15, {0: "Fizz 🍹", 5: "Buzz 🐝"}.get(num % 5, num))
    print(output)

#4. List Comprehension Challenge 🧠
# Create a list of squares of numbers from 1 to 10 using list comprehension.

square = [x**2 for x in range(11)]
print(square)

