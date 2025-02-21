# Day 10: Data Visualization with Matplotlib & Seaborn

import matplotlib.pyplot as plt  # For basic plotting
import seaborn as sns  # For advanced visualizations
import numpy as np  # For numerical operations
import pandas as pd  # For handling datasets


# 1. Creating Basic Plots 
    # Line Plot (Trend over Time)

# Sample Data
x = [1, 2, 3, 4, 5]  # X-axis values (e.g., months)
y = [10, 15, 7, 20, 25]  # Y-axis values (e.g., revenue in $1000s)

# Create Line Plot
plt.plot(x, y, marker='o', linestyle='-', color='b', label="Sales Trend")  

# Adding Labels and Title
plt.xlabel("Time (Months)")  # X-axis label
plt.ylabel("Revenue ($1000s)")  # Y-axis label
plt.title("Company Sales Over Time")  # Title of the plot
plt.legend()  # Show legend

# Display the Plot
plt.show()


    # Bar Chart (Comparison of Categories)

# Sample Data
categories = ["A", "B", "C", "D"]  # Category names
values = [40, 70, 30, 90]  # Values for each category

# Create Bar Chart
plt.bar(categories, values, color='g')  

# Title and Labels
plt.xlabel("Categories")  # Label for X-axis
plt.ylabel("Performance Score")  # Label for Y-axis
plt.title("Category Performance")  # Title of the chart

# Show the Plot
plt.show()


    # Scatter Plot (Relationship Between Two Variables)
# Generate random data
x = np.random.rand(50)  # Random X values
y = np.random.rand(50)  # Random Y values

# Create Scatter Plot
plt.scatter(x, y, color='r')

# Titles & Labels
plt.xlabel("X values")  
plt.ylabel("Y values")  
plt.title("Random Data Scatter Plot")

# Show Plot
plt.show()

# 2. Histograms & Distribution Plots 

    # Histogram (Data Distribution)

# Generate 1000 random numbers from a normal distribution
data = np.random.randn(1000)

# Create Histogram
plt.hist(data, bins=30, color='purple', alpha=0.7)  # bins=30 sets the number of bars

# Titles & Labels
plt.xlabel("Value Ranges")  
plt.ylabel("Frequency")  
plt.title("Histogram of Random Data")

# Show Plot
plt.show()

    # Create histogram with a KDE (Kernel Density Estimate) line
sns.histplot(data, bins=30, kde=True, color="blue")

# Title
plt.title("Distribution Plot with KDE")

# Show Plot
plt.show()

# 3. Heatmaps (Correlation Analysis)

# Create sample dataset with 3 features
data = {
    "Feature A": np.random.rand(10),
    "Feature B": np.random.rand(10),
    "Feature C": np.random.rand(10)
}
df = pd.DataFrame(data)  # Convert dictionary to DataFrame

# Create Heatmap for correlation between features
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")  

# Title
plt.title("Heatmap of Feature Correlations")

# Show Plot
plt.show()

# 4. Customizing & Saving Plots 🎨
plt.figure(figsize = (8, 5)) # Width = 8, Height = 5
plt.grid(True) # Show grid on the plot
plt.savefig("my_plot.png", dpi = 300) 


# Challenge of the day!

# 1️. Load a dataset using Pandas 📂
df = pd.read_csv("data.csv")
print(df.head())

# 2️. Create a scatter plot showing the relationship between two numerical columns
plt.scatter(df["Age"], df["Salary"], color = 'b')
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age / Salary Diagramm")
plt.show()

# 3️. Generate a histogram to show the distribution of one numerical column
sns.histplot(df["Age"], bins = 30, color= 'b')
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Title")
plt.show()

# 4️. Create a heatmap to visualize correlations between multiple numerical columns
correlation_matrix = df.corr()

sns.heatmap(correlation_matrix, annot = True, cmap= True)

plt.title("Heatmap of Feature Correlations")
plt.show()

# 5️. Customize your plots (titles, colors, labels)
# Load dataset
df = pd.read_csv("data.csv")

# Check the column names to replace placeholders
print(df.columns)  # This will show you the actual column names in your dataset

# Customizing a scatter plot
plt.figure(figsize=(10, 6))  # Set figure size (Width = 10, Height = 6)
plt.scatter(df["age"], df["income"], color='green', alpha=0.6, label='Data Points')

# Adding title, labels, and gridlines
plt.title("Customized Scatter Plot: Age vs Income", fontsize=16, color='blue')
plt.xlabel("Age", fontsize=12)
plt.ylabel("Income", fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # Adding gridlines

# Adding legend
plt.legend()

# Save the plot as an image
plt.savefig("custom_scatter_plot.png", dpi=300)  # Save with 300 dpi resolution

# Show the plot
plt.show()