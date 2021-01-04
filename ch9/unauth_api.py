# coding: utf-8
# APIs save you trouble from having to scrap your data
# HTTP is a protocol for transfering text data, so all data through a Web API is serialized into string (text) format

from dateutil.parser import parse
from collections import Counter
import requests
import json

serialized = """{ "title" : "Data Science Book",
                  "author" : "Joel Grus",
                  "publicationYear" : 2019,
                  "topics" : [ "data", "science", "data science"] }"""

type(serialized)  # string

# parse JSON to create a Python dict
# use json module and the loads function
deserialized = json.loads(serialized)

type(deserialized)  # dict

assert deserialized['publicationYear'] == 2019
assert "data science" in deserialized['topics']

# most APIs require authentication, so use GitHub's API
github_user = "paulapivat"
endpoint = f"https://api.github.com/users/{github_user}/repos"
repos = json.loads(requests.get(endpoint).text)

type(repos)  # list

# loop through repos, grab all "url" keys
for repo in repos:
    print(repo['url'])

##### ------ Access GitHub public API ------######


dates = [parse(repo['created_at']) for repo in repos]
month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)
last_5_repositories = sorted(repos,
                             key=lambda r: r['pushed_at'],
                             reverse=True)[:5]

# ['Python', 'HTML', 'R', 'R', 'R']
last_5_languages = [repo['language'] for repo in last_5_repositories]

last_5_repositories
print(dates)
