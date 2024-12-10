import pandas as pd
import numpy as np

# Load data from a CSV file
data = pd.read_csv('data.csv')

# Clean the data
data.dropna(inplace=True)

# Perform data analysis
mean_value = data['column_name'].mean()
std_dev = data['column_name'].std()

# Print the results
print("Mean:", mean_value)
print("Standard Deviation:", std_dev)
