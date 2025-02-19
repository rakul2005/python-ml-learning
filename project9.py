# Day 9: Pandas Basics - Data Handling & Analysis

# 1. Working with Series 

import pandas as pd

data = [10, 20, 30, 40, 50]
series = pd.Series(data)

print(series)

# 2. Working with DataFrames 

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25,30,35],
    "City": ["New York", "London", "Berlin"]
}

df = pd.DataFrame(data)
print(df)

# 3. Reading & Writing Data

# Reading CSV Files:
df = pd.read_csv("data.csv")
print(df.head())

# Writing CSV Files:
df.to_csv("output.csv", index=False)

# Reading JSON Files:
df = pd.read_json("data.json")

# 4. Selecting & Filtering Data

# Selecting a single column:
print(df["Age"])

# Filtering rows (e.g., people older than 30):

filtered_df = df[df["Age"] > 30]
print(filtered_df)

# 6️. Modifying & Cleaning Data 

# Adding a new column
df["Salary"] = [50000, 60000, 70000, 80000, 90000]  # 5 values for 5 rows

# Removing missing values
df.dropna(inplace = True)

# Renaming columns
df.rename(columns={"Name":"Full Name"},inplace=True)

# Challenge of the Day!

# Step 1: Load the CSV file
df = pd.read_csv("data.csv")  # Make sure "data.csv" exists in your working directory

# Step 2: Find the average age
average_age = df["Age"].mean()
print("Average Age:", average_age)

# Step 3: Filter people younger than 30
filtered_df = df[df["Age"] < 30]

# Step 4: Save the filtered data to a new CSV file
filtered_df.to_csv("filtered_data.csv", index=False)

print("Filtered data saved to 'filtered_data.csv' successfully!")
