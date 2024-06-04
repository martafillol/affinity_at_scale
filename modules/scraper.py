import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://medium.com/@getgoing.ca/the-ultimate-guide-to-choosing-the-perfect-car-19747eec95e'

def scraper(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    scraped_data = []
    html_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']
    for tag in html_tags:
        elements = soup.find_all(tag)
        texts = [element.text.strip() for element in elements if len(element.text.strip()) > 30]
        scraped_data.extend(texts)

    scraped_data = pd.Series(scraped_data)

    return scraped_data


if __name__ == "__main__":
    print(scraper(url))
