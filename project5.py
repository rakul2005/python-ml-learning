# Day 5: Exception Handling in Python ⚡
#Exceptions are errors that occur during program execution. Handling them properly prevents crashes and ensures smooth code execution.

# 1. Exceptions

print(10 / 0) # ZeroDivisionError

# 2. Handling Exceptions with try-except

try: 
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print(" You cannot divide by zero!")
except ValueError:
    print(" Please enter a valid number")

# 3. Using else and finally in Exception Handling

try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print(" File not found!")
else:
    print(" File read successfully!")
finally:
    file.close()
    print(" Closing file...")

# 4. Raising Custom Exceptions (raise)

age = int(input("Enter your age: "))


if age < 18:
    raise ValueError(" You must be 18 or older!")

##### 5. Exception Handling Best Practices

    # 1. Write a program that asks for two numbers and divides them.

try:
    x = float(int(input("Enter a number: ")))
    y = float(int(input("Enter a second number: ")))
    
    z = x / y

    print(f"The result of {x} / {y} is: {z}")

except ZeroDivisionError:
    print("You cannot divide by zero. Try again!")

except ValueError:
    print("Invalid input! Try only with numbers")

finally:
    print("Success!")

    # 2️. File Handling with Error Checking 📂

try:
    file = open("data.txt", "r")
    content = file.read()

except FileNotFoundError:
    print("file is not found, try again!")
else:
    print("file is found successfully!")

finally:
    file.close()
    print("file closing...")

# 3️. Bank Withdrawal System 🏦

try:
    total = float(int(input("Enter your total account balance: ")))

    withdraw = float(int(input("Enter the amount to withdraw: ")))

    if withdraw > total:
        raise ValueError(" Insufficient funds! Cancelled withdrawal")
    
    total -= withdraw
    print(f"Withdrawal successful! Remaining balance: ${total:.2f}")

except ValueError as e:
    print(e)

finally:
    print("Transaction complete")

# 4️. Custom Age Validator 

age = int(input("Enter your age: "))

if age < 0 or age > 150:
    raise ValueError("Enter a valid age!")










