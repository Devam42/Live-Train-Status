import requests
from bs4 import BeautifulSoup

def get_data(url):
    # Send an HTTP GET request to fetch the webpage content
    r = requests.get(url)
    return r.text

# URL of the live train status page
url = "https://www.railyatri.in/live-train-status/12801?start_day=1"

# Fetch the HTML data
html_data = get_data(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_data, 'html.parser')

# Print the parsed HTML (optional, for debugging purposes)
print(soup.prettify())

# Save the entire HTML content to a file named 'html.txt'
with open("html.txt", "w", encoding='utf-8') as file:
    file.write(soup.prettify())

print("HTML content saved to 'html.txt'")
