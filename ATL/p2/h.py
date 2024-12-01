# pip install pandas matplotlib seaborn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a more complex dataset using Pandas
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack'],
    'Age': [23, 35, 45, 29, 50, 32, 41, 38, 28, 47],
    'Salary': [70000, 80000, 120000, 90000, 150000, 105000, 98000, 76000, 132000, 115000],
    'Department': ['HR', 'Engineering', 'Management', 'Sales', 'Engineering', 'Marketing', 'Sales', 'HR', 'Management', 'Engineering']
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Data:")
print(df)

# Basic Analytics: Calculate the average, median, and standard deviation of salary
average_salary = df['Salary'].mean()
median_salary = df['Salary'].median()
std_dev_salary = df['Salary'].std()

print("\nBasic Analytics:")
print(f"Average Salary: {average_salary}")
print(f"Median Salary: {median_salary}")
print(f"Salary Standard Deviation: {std_dev_salary}")

# Correlation between Age and Salary
correlation = df['Age'].corr(df['Salary'])
print(f"\nCorrelation between Age and Salary: {correlation}")

# Filter Data: Find people with salary above 80,000
high_salary = df[df['Salary'] > 80000]
print("\nPeople with salary above 80,000:")
print(high_salary)

# Data Visualization: Create multiple plots

# 1. Bar plot for salary by employee
plt.figure(figsize=(10, 6))
plt.bar(df['Name'], df['Salary'], color='skyblue')
plt.title('Employee Salaries')
plt.xlabel('Employee')
plt.ylabel('Salary')
plt.xticks(rotation=45)
plt.show()

# 2. Histogram for salary distribution
plt.figure(figsize=(10, 6))
plt.hist(df['Salary'], bins=5, color='lightcoral', edgecolor='black')
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

# 3. Scatter plot for Age vs Salary
plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['Salary'], color='green')
plt.title('Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.grid(True)
plt.show()

# 4. Box plot for salary by department
plt.figure(figsize=(10, 6))
sns.boxplot(x='Department', y='Salary', data=df, palette="Set2")
plt.title('Salary Distribution by Department')
plt.show()
