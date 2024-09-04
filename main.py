import requests
from bs4 import BeautifulSoup

# URL of the BBC News website
url = "https://www.bbc.com/news"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the headlines in the page (h2 elements)
    headlines = soup.find_all('h2')

    # Loop through the headlines and print each one
    for headline in headlines:
        print(headline.get_text())
        print('--------------------------------------')
else:
    # Print an error message if the request failed
    print("Failed to retrieve the webpage.")