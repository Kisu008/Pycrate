import requests
from bs4 import BeautifulSoup

# URL of the Awesome Python list on GitHub
url = 'https://github.com/vinta/awesome-python'

# Send a GET request to the URL and get the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the section containing the curated list of Python libraries and tools
section = soup.find('article', {'class': 'markdown-body entry-content container-lg'})

# Find all the <h2> tags containing the names of the libraries and tools
h2_tags = section.find_all('h2')

# Extract the names of the libraries and tools from the <h2> tags and store them in a list
library_names = [tag.text for tag in h2_tags]

# Print the list of library names
print("Curated List of Python Libraries and Tools:\n")
for i, name in enumerate(library_names):
    print(f"{i+1}. {name}")