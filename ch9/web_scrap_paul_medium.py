# coding: utf-8
from typing import Dict, Set
import re
from bs4 import BeautifulSoup
import requests
url = "https://paulapivat.medium.com/"
text = requests.get(url).text
soup = BeautifulSoup(text, 'html5lib')
soup
all_urls = [a['href'] for a in soup('a') if a.has_attr('href')]
print(len(all_urls))
all_urls
