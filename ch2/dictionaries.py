# coding: utf-8
empty_dict = {}
type(empty_dict)
empty_dict2 = dict()
type(empty_dict2)
grades = {"Joel": 80, "Grus": 99}
type(grades)
grades["Grus"]
grades["Joel"]
grades["Tim"] = 93
grades
try:
    kate_grades = grades["Kate"]
except KeyError:
    print("That key doesn't exist")
    
grades
joe_has_grade = "Joel" in grades
joe_has_grade
kate_does_not = "Kate" in grades
kate_does_not
grades.get("Joel")
grades.get("Grus")
grades.get("Kate")
grades.get("No one")
grades
grades["Grus"] = 97
grades
grades["Kate"] = 88
grades
len(grades)
tweet = {
    "user": "paulapivat",
    "text": "Reading Data Science from Scratch",
    "retweet_count": 100,
    "hashtags": ["#66daysofdata", "datascience", "machinelearning", "python", "R"]
    }
tweet
tweet["retweet_count"]
tweet["hashtags"]
tweet["user"]
tweet["hashtags"][2]
tweet_keys = tweet.keys()
tweet_keys
type(tweet_keys)
type(tweet)
for key,value in tweet_items:
    print(key)
    
for key,value in tweet_items:
    print("These are the keys:", key)
    print("These are the values:", value)
    
for key, value in tweet_items:
    print(key)
    
for key, value in enumerate(tweet):
    print(value)
    
for key, value in enumerate(tweet):
    print(key)
    
for key, value in enumerate(tweet):
    print(key)
    print(value)
    
"user" in tweet
"bball" in tweet
"python" in tweet
"python" in tweet_values
tweet_values
"python" in tweet.values()
"paulapivat" in tweet_values
tweet
100 in tweet_values
'python' in tweet_values
"hashtags" in tweet
'python' in tweet['hashtags']
