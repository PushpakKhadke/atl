# pip install numpy pandas matplotlib


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create a simple dataset using Pandas
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [23, 35, 45, 29, 50],
    'Salary': [70000, 80000, 120000, 90000, 150000]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Data:")
print(df)

# Basic Analytics: Calculate the average salary
average_salary = df['Salary'].mean()
print("\nAverage Salary:", average_salary)

# Filter Data: Find people with salary above 80,000
high_salary = df[df['Salary'] > 80000]
print("\nPeople with salary above 80,000:")
print(high_salary)

# Data Visualization: Create a bar plot for salary
plt.bar(df['Name'], df['Salary'], color='skyblue')
plt.title('Employee Salaries')
plt.xlabel('Employee')
plt.ylabel('Salary')
plt.show()
