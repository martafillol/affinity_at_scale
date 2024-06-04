import requests
from bs4 import BeautifulSoup
import pandas as pd
import spacy
from spacymoji import Emoji

url = 'https://medium.com/@getgoing.ca/the-ultimate-guide-to-choosing-the-perfect-car-19747eec95e'

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("emoji", first=True)


def scrape(url):
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

scrape_data = scrape(url)

def text_cleaner(text):
    serie_joined = ' '.join(text)
    doc = nlp(serie_joined)
    clean_words = []
    for each in doc:
        if each._.is_emoji or each.is_digit or each.like_url or each.like_email or each.is_punct:
            continue
        else:
            clean_words.append(each)

    return clean_words
#Use scraper for multiple websites:
def scraper(lst):
    list = []
    for l in lst:
        scr = scrape(l)
        clt = text_cleaner(scr)
        list.extend(clt)
    return list
