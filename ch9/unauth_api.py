# coding: utf-8
# APIs save you trouble from having to scrap your data
# HTTP is a protocol for transfering text data, so all data through a Web API is serialized into string (text) format

from twython import TwythonStreamer
from twython import Twython
import webbrowser
import os
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

###### TWITTER API ######


# Plug in your key and secret directly
CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY")         # API Key
CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET")   # API Secret Key


# Get a temporary client to retrieve an authentication URL
temp_client = Twython(CONSUMER_KEY, CONSUMER_SECRET)
temp_creds = temp_client.get_authentication_tokens()
url = temp_creds['auth_url']

# Visit that URL to authorize the application and get a PIN
print(f"go visit {url} and get the PIN code and paste it below")
webbrowser.open(url)
PIN_CODE = input("please enter the PIN code: ")

# Use that PIN_CODE to get the actual tokens
auth_client = Twython(CONSUMER_KEY,
                      CONSUMER_SECRET,
                      temp_creds['oauth_token'],
                      temp_creds['oauth_token_secret'])

final_step = auth_client.get_authorized_tokens(PIN_CODE)
ACCESS_TOKEN = final_step['oauth_token']
ACCESS_TOKEN_SECRET = final_step['oauth_token_secret']

# Get a new Twython instance using them
twitter = Twython(CONSUMER_KEY,
                  CONSUMER_SECRET,
                  ACCESS_TOKEN,
                  ACCESS_TOKEN_SECRET)

# Once we have an authenticated Twython instance, we can perform searches

# Search for tweets containing the phrase 'data science' (Latest tweets at time of running this loop)
for status in twitter.search(q='"data science"')["statuses"]:
    user = status["user"]["screen_name"]
    text = status["text"]
    print(f"{user}: {text}\n")

# Instead of the 'Latest Tweets' we want Streaming API to get a sample of lots of tweets
# First we need to define a class that inherits from TwythonStreamer
# and overrides its on_success method
# and possibly its on_error method


# Appending data to a global variable is poor form
# but it makes the example much simpler

tweets = []


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        """
        What do we do when Twitter sends us data?
        Here data will be a Python dict representing a tweet.
        """
        # We only want to collect English-language tweets
        if data.get('lang') == 'en':
            tweets.append(data)
            print(f"received tweet #{len(tweets)}")
        # Stop when we've collected enough
        if len(tweets) >= 100:
            self.disconnect()

    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()


stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET,
                    ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# starts consuming public statuses that contain the keyword 'data'

# will receive tweet #1 - #100; see tweets list
stream.statuses.filter(track='data')

# if we want to consume a sample of *all* public statuses
# stream.statuses.sample()


top_hashtags = Counter(hashtag['text'].lower()
                       for tweet in tweets
                       for hashtag in tweet['entities']['hashtags'])

# [('pennsylvania', 3), ('data', 3), ('stopthesteai', 2), ('analytics', 2), ('100daysofcode', 2)]
print(top_hashtags.most_common(5))

# NOTE: in a real project you wouldn't use an in-memory list, but rather a data base to store tweets permanently
