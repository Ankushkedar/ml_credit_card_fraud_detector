import requests
from bs4 import BeautifulSoup

# Specify the URL to scrape
url = "https://www.example.com"

# Fetch the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract specific data
titles = soup.find_all('h2')
for title in titles:
    print(title.text)

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

