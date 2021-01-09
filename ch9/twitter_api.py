# for python-dotenv method of access environment variables
from twython import Twython
from twython import TwythonStreamer
from collections import Counter
import webbrowser
import os
import dotenv
from dotenv import load_dotenv
load_dotenv()

###### TWITTER API ######

print("Start Twitter API...")

# IMPORTANT: PLUG YOUR KEY AND SECRET IN DIRECTLY (without os.environ.get())
CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY")         # API Key
CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET")   # API Secret Key


# Get a temporary client to retrieve an authentication URL
temp_client = Twython(CONSUMER_KEY, CONSUMER_SECRET)
temp_creds = temp_client.get_authentication_tokens()
url = temp_creds['auth_url']

# Visit that URL to authorize the application and get a PIN
print(f"go visit {url} and get the PIN code and paste it below")
webbrowser.open(url)

# Possible to Skip lines 17-18 and start here? #
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


# Store top 20 mentions using twython endpoints get_mentions_timeline()

# create empty list
mentions = list()

mentions = twitter.get_mentions_timeline()

# loop through to grab text
for dct in mentions:
    for k,v in dct.items():
        if k == 'text':
            print(v)

# Collection of 19 Recent Tweets/Retweets by me and my followers; get_home_timeline()
home_timeline = list()

# Find names of people I follow who are recently on my home_timeline
for dct in home_timeline:
    for k,v in dct.items():
        if k == 'user':
            for k_i, v_i in v.items():
                if k_i == 'name':
                    print(v_i)


