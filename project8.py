# Day 8: Introduction to NumPy 📊

# 1️. NumPy Basics: Creating Arrays

import numpy as np

# 1D Array
arr1 = np.array([1, 2, 3, 4])

# 2D Array (Matrix)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# array of zeros
zeros = np.zeros((3, 3))

# array of ones
ones = np.ones((2, 2))

# array with a range of numbers
range_array = np.arange(1, 11, 2)  # [1, 3, 5, 7, 9]

# linearly spaced array
linspace_array = np.linspace(0, 10, 5) # [0. , 2.5, 5. , 7.5, 10. ]

# 2️. Indexing & Slicing in NumPy

arr = np.array([10, 20, 30, 40, 50])

# Accessing elements
print(arr[0])   # 10
print(arr[-1])  # 50

# Slicing
print(arr[1:4])  # [20, 30, 40]
print(arr[:3])   # [10, 20, 30]
print(arr[::2])  # [10, 30, 50] (step = 2)

# For multi-dimensional arrays

arr2 = np.array([[1,2,3], [4,5,6], [7,8,9]])

print(arr2[1,2])    # 6 (row 1, column 2, prints: 6)
print(arr2[:,0])    # [1, 4, 7] (all rows, first column [1 4 7])

# 3️. NumPy Array Operations

arr3 = np.array([1, 2, 3, 4, 5])

# Element-wise operations
print(arr3 + 10)    # [11 12 13 14 15]
print(arr3 * 2)     # [ 2 4 6 8 10]
print(arr3 ** 2)    # [1 4 9 16 25]

# Applying NumPy functions
print(np.sqrt(arr3)) # [1. 1.414 1.732 2. 2.236]
print(np.log(arr3))  # [natural log]
print(np.exp(arr))   # exponential


# 4️. Statistical Functions in NumPy
arr4 = np.array([10, 20, 30, 40, 50])

print("Mean:", np.mean(arr4))
print("Sum:", np.sum(arr4))
print("Min:", np.min(arr4))
print("Max:", np.max(arr4))
print("Standard Deviation:", np.std(arr4))

# 5️. Reshaping & Stacking Arrays
arr5 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# reshape into a 3x3 matrix

arr2D = arr5.reshape((3,3))
print(arr2D)

# Flatten an array
flat_arr = arr2D.flatten()

# Stacking arrays
arr6 = np.array([1,2,3])
arr7 = np.array([4,5,6])

print(np.hstack((arr6, arr7)))
print(np.vstack((arr6, arr7)))

# Challenge of the Day!

# array from 1 to 50
arr8 = np.arange(1, 51)

# mean, max, min
print("Mean:", np.mean(arr8))
print("Max:", np.max(arr8))
print("Min:", np.min(arr8))

# square root
sqrt_arr8 = np.sqrt(arr8)
print("Square Roots:", sqrt_arr8)

# reshape into a 5x10 matrix
reshaped_arr8 = arr.reshape(5, 10)
print("Reshaped Array:")
print(reshaped_arr8)