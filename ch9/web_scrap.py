# coding: utf-8
import bs4
bs4.__version__
from bs4 import BeautifulSoup
import requests
url = ("https://raw.githubusercontent.com/"
       "joelgrus/data/master/getting-data.html")
url
html = requests.get(url).text
html
soup = BeautifulSoup(html, 'html5lib')
soup
# find first <p> tag
first_paragraph = soup.find('p')
first_paragraph
# get text content of a tag
first_paragraph_text = soup.p.text
first_paragraph_text
type(first_paragraph_text)
first_paragraph_words = soup.p.text.split()
first_paragraph_words
first_paragraph_words[3]
# extract a tag's attributes by treating it like a dict
first_paragraph_id = soup.p['id']     
first_paragraph_id
first_paragraph_id2 = soup.p.get('id')
first_paragraph_id2
soup.p.get('class')
first_paragraph_class = soup.p.get('class')
first_paragraph_class
soup.p['class']
all_paragraphs = soup.find_all('p')
all_paragraphs
app_paragraphs[1]
all_paragraphs[1]
paragraphs_with_ids = [p for p in soup('p') if p.get('id')]
paragraphs_with_ids
# find tags with specific classes
important_paragraphs = soup('p', {'class': 'important'})
important_paragraphs
important_paragraphs2 = soup('p', 'important')
important_paragraphs2
important_paragraphs3 = [p for p in soup('p')
                         if 'important' in p.get('class', [])]
important_paragraphs3
