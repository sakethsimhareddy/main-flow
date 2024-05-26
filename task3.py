import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
url = "https://realpython.github.io/fake-jobs"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the title of the webpage
title = soup.find('title').text if soup.find('title') else 'No title found'
print("Title:", title)

# Extract all links from the webpage
links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))
print("Links:")
for link in links:
    print(link)

# Extract all images from the webpage
images = []
for img in soup.find_all('img'):
    images.append(img.get('src'))
print("Images:")
for img in images:
    print(img)

# Extract text from the page
text = soup.get_text(separator=' ', strip=True)
print("Text:",text)
