# coding: utf-8
from bs4 import BeautifulSoup
import requests
url = "https://www.house.gov/representatives"
text = requests.get(url).text
text
soup = BeautifulSoup(text, 'html5lib')
soup
all_urls = [a['href'] for a in soup('a') if a.has_attr('href')]
print(len(all_urls))
all_urls
# We want ones that start with either http:// or https://, have a person's name, or end with .house.gov or house.gov/
# use regular expressions
import re
# must start with http:// or https://
# must end with house.gov or house.gov/
regex = r"^https?://.*\.house\.gov/?$"
# Write some tests
assert re.match(regex, "http://paul.house.gov")
assert re.match(regex, "https://paul.house.gov")
assert re.match(regex, "http://paul.house.gov/")
assert re.match(regex, "https://paul.house.gov/")
assert not re.match(regex, "paul.house.gov")
assert not re.match(regex, "http://paul.house.com")
assert not re.match(regex, "https://paul.house.gov/biography")
# apply regex in list comprehension
good_urls = [url for url in all_urls if re.match(regex, url)]
print(len(good_urls))
# use 'set' to get rid of duplicate urls
good_urls = list(set(good_urls))
print(len(good_urls))
good_urls
html = request.get('https://pelosi.house.gov').text
html = requests.get('https://pelosi.house.gov').text
soup = BeautifulSoup(html, 'html5lib')
soup
# use a set because links might appear multiple times
links = {a['href'] for a in soup('a') if 'press releases' in a.text.lower()}
print(links)
# this is a relative link, so we need to remember to originating site
from typing import Dict, Set
press_releases: Dict[str, Set[str]] = {}
for house_url in good_urls:
    html = requests.get(house_url).text
    soup = BeautifulSoup(html, 'html5lib')
    pr_links = {a['href'] for a in soup('a') if 'press releases' in a.text.lower()}
    print(f"{house_url}: {pr_links}")
    press_releases[house_url] = pr_links
    
get_ipython().run_line_magic('save', 'web_scrap_congress.py 1-43')
