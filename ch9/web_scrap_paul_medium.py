# coding: utf-8
from typing import Dict, Set
import re
from bs4 import BeautifulSoup
import requests

url = "https://paulapivat.medium.com/"
text = requests.get(url).text
soup = BeautifulSoup(text, 'html5lib')

all_urls = [a['href'] for a in soup('a') if a.has_attr('href')]
print(len(all_urls))      # 125

unique_urls = list(set(all_urls))
print(len(unique_urls))   # 111

# We want ones that start with either http:// or https://,
# ex: http://towardsdatascience.com
# use regular expressions
# must start with http:// or https://
# must end with .com or .com/

tds_regex = r"^https?://towardsdatascience.com/?$"

# write tests
assert re.match(tds_regex, "http://towardsdatascience.com")
assert re.match(tds_regex, "https://towardsdatascience.com")
assert re.match(tds_regex, "http://towardsdatascience.com/")
assert re.match(tds_regex, "https://towardsdatascience.com/")
assert not re.match(tds_regex, "towardsdatascience.com")
assert not re.match(tds_regex, "http://towardsdatascience.net")
assert not re.match(tds_regex, "https://towardsdtaaascience.com")

# apply regex to list comprehension

word = 'towardsdatascience.com'

tds_urls = [url for url in unique_urls if word in url]
print(len(tds_urls))
