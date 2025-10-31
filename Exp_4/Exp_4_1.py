# Q1. 1. Write a python program to import and export data using pandas and show the detail of the data set like number of rows column , first five row, number of missing value, sum , avg,min and max value.
import pandas as pd

# Import the data form the CSV file
data = pd.read_csv('Iris.csv')

# Printing number of rows
print("Number of rows: ",data.shape[0])

# Printing number of column
print("Number of column: ",data.shape[1])

# Display the First Five rows
print("\nFirst five rows of the dataset: ")
print(data.head())

# Display the last five rows 
print("Last five rows of the dataset: ")
print(data.tail())

#Display the missing values
print("\nNumber of missing values in each column: ")
print(data.isnull().sum())
#Display the sum of numerical columns
print("\nSum of numerical column: ")
print(data.sum(numeric_only= True))
#Display the Avg
print("\nAverage of numerical column:")
print(data.mean(numeric_only=True))
#Display Minimum values of numerical column
print("\nMinimum value of numerical columns: ")
print(data.min(numeric_only=True))
#Display Maximum value of numerical columns
print("\nMaximum value of numerical columns: ")
print(data.max(numeric_only=True))

# data.to_csv('clean_data.csv',index=False)
