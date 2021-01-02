# coding: utf-8
import bs4
from bs4 import BeautifulSoup
import requests

url = ("https://raw.githubusercontent.com/"
       "joelgrus/data/master/getting-data.html")

html = requests.get(url).text

soup = BeautifulSoup(html, 'html5lib')

# find first <p> tag
first_paragraph = soup.find('p')

# get text content of a tag
first_paragraph_text = soup.p.text

first_paragraph_words = soup.p.text.split()

first_paragraph_words[3]
# extract a tag's attributes by treating it like a dict
first_paragraph_id = soup.p['id']

first_paragraph_id2 = soup.p.get('id')


all_paragraphs = soup.find_all('p')
all_paragraphs

all_paragraphs[1]
paragraphs_with_ids = [p for p in soup('p') if p.get('id')]
paragraphs_with_ids

# find tags with specific classes
important_paragraphs = soup('p', {'class': 'important'})

important_paragraphs2 = soup('p', 'important')

important_paragraphs3 = [p for p in soup('p')
                         if 'important' in p.get('class', [])]
