# Day 6: File Handling in Python 

# 1️. Opening & Reading a File 
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("File not found!")

# 2️. Writing to a File 

file = open("output.txt", "w")
file.write("Hello, File Handling!")
file.close

# 3️. Appending to a File

file = open("output.txt", "a")
file.write("\nNew line added!")
file.close()

# 4️. Reading Files Line by line

file = open("data.txt", "r")
for line in file.readlines():
    print(f"{line.strip()}")
file.close()

# 5️. Using with Statement (Best Practice)

with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# Challenge of the Day! (practice)
# File Logging System

try:
        # Ask user for their name and age
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    # Open the file in append mode ("a") to add new data without overwriting
    with open("users.txt", "a") as file:
        file.write(f"{name}, {age}\n")

    print("User saved successfully!")
    
    # Read and print all stored users
    print("\n Saved users:")
    with open("users.txt", "r") as file:
        print(file.read())

except ValueError:
    print("Invalid input!")

except Exception as e:
    print(f"Invalid input: {e}")                  


























