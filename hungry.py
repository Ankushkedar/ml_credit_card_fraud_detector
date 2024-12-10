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
