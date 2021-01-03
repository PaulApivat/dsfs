# coding: utf-8
from typing import Dict, Set
import re
from bs4 import BeautifulSoup
import requests
url = "https://www.house.gov/representatives"
text = requests.get(url).text

soup = BeautifulSoup(text, 'html5lib')

all_urls = [a['href'] for a in soup('a') if a.has_attr('href')]
print(len(all_urls))


# We want ones that start with either http:// or https://, have a person's name, or end with .house.gov or house.gov/
# use regular expressions
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


html = requests.get('https://pelosi.house.gov').text
soup = BeautifulSoup(html, 'html5lib')

# use a set because links might appear multiple times
links = {a['href'] for a in soup('a') if 'press releases' in a.text.lower()}
print(links)
# this is a relative link, so we need to remember to originating site
press_releases: Dict[str, Set[str]] = {}

for house_url in good_urls:
    html = requests.get(house_url).text
    soup = BeautifulSoup(html, 'html5lib')
    pr_links = {a['href']
                for a in soup('a') if 'press releases' in a.text.lower()}
    #print(f"{house_url}: {pr_links}")
    press_releases[house_url] = pr_links


def paragraph_mentions(text: str, keyword: str) -> bool:
    """
    Returns true if a <p> inside text mentions (keyword)
    """
    soup = BeautifulSoup(text, 'html5lib')
    paragraphs = [p.get_text() for p in soup('p')]
    return any(keyword.lower() in paragraph.lower() for paragraph in paragraphs)


text = """<body><h1>Facebook</h1><p>Twitter</p>"""
assert paragraph_mentions(text, "twitter")  # is inside a <p>
assert not paragraph_mentions(text, "facebook")  # not inside a <p>

# Find the relevant congresspeople and give their names to the VP
for house_url, pr_links in press_releases.items():
    for pr_link in pr_links:
        url = f"{house_url}/{pr_link}"
        text = requests.get(url).text
        if paragraph_mentions(text, 'data'):
            print(f"{house_url}")
            break  # done with this house_url
