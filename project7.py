# Day 7: Object-Oriented Programming (OOP) in Python 

# 1. Defining Classes & Creating Objects
#    Example: A Car Class 

# Defining a class
class Car:
    def __init__(self, brand, model, year): # Constructor
        self.brand = brand # Attribute
        self.model = model
        self.year = year

    def display_info(self): # Method
        print(f"🚗 {self.year} {self.brand} {self.model}")

# Creating objects
car1 = Car("Tesla", "Model S", 2023)
car2 = Car("BMW", "M3", 2022)

# Using methods
car1.display_info() # Output: 2023 Tesla Model S
car2.display_info() # Output: 2022 BMW M3

# 2. Inheritance (Reusing Code)
class ElectricCar(Car): # Child class inherits from Car
    def __init__(self, brand, model, year, battery_size, charging_speed):
        super().__init__(brand, model, year) # Call parent constructor
        self.battery_size = battery_size # New attribute
        self.charging_speed = charging_speed

    def battery_info(self):
        print(f"Battery size: {self.battery_size} kWh")

    def charging_info(self):
        print(f"Charging speed: {self.charging_speed} min")

# Creating an object of ElectricCar
ev = ElectricCar("Tesla", "Model 3", 2023, 75, 495)
ev.display_info()
ev.battery_info()
ev.charging_info()

# 3. Polymorphism (Multiple Forms)

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"
    
class Bird:
    def speak(self):
        return "Beep Beep!"
    
# Polymorphism in action

animals = [Dog(), Cat(), Bird()]
for animal in animals:
    print(animal.speak())

# 4. Encapsulation (Protecting Data)

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance 

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited ${amount}, New Balance: ${self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        
        else:
            self.__balance -= amount
            print(f"Withdrawn ${amount}, Remaining balance: ${self.__balance}")

# Creating an account
account = BankAccount(500)
account.deposit(200)
account.withdraw(800)

# Challenge of the Day

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Doctor(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender

    def gender_info(self):
        print(f"Gender: {self.gender}")

doctor = Doctor("doc", 59, "Male")

class Patient(Person):
    def __init__(self, name, age, disease):
        super().__init__(name, age)
        self.disease = disease

    def disease_info(self):
        print(f"Disease: {self.disease}")

patient = Patient("patient", "29", "Asthma")

doctor.display_info()
doctor.gender_info()
patient.display_info()
patient.disease_info()
