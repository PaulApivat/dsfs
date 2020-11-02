# coding: utf-8
get_ipython().run_line_magic('run', 'friendship_network.py')
friendships
"""find total number of connections, sum length of all friends lists"""
def number_of_friends(user):
    """How many friends does _user_ have?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)
    
total_connections = sum(number_of_friends(user) for user in users)
total_connections
num_users = len(users)
num_users
avg_connections = total_connections / num_users
avg_connections
"""find most connected people - largest num of friends - via sorting"""
"""Create a list (user_id, number_of_friends)"""
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
num_friends_by_id
num_friends_by_id.sort(
    key=lambda id_and_friends: id_and_friends[1],
    reverse=True)
num_friends_by_id
"""Each pair is (user_id, num_friends)"""
"""Just computed Degree Centrality"""
"""Data Scientists You May Know"""
def foaf_ids_bad(user):
    """foaf is short for 'friend of a friend' """
    return [foaf_id
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]
            
users[0]
print(friendships[0])
print(friendships[1])
print(friendships[2])
""" produce a count of mutual friends, exclude people already known to user"""
from collections import Counter
def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id
        and foaf_id not in friendships[user_id]
        )
        
print(friends_of_friends(users[3]))
"""interest data in the form of list of tuple"""
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming langauges"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
    ]
"""built a function to find users with certain interests"""
def data_scientists_who_like(target_interest):
    """Find the ids of all users who like the target interests."""
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]
            
data_scientists_who_like("Python")
"""build an index from interests to users"""
from collections import defaultdict
"""keys are interests, values are lists of user_ids with that interests"""
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
    
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
    
user_ids_by_interest["Python"]
"""create another list from users to interest"""
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)
    
interests_by_user_id[9]
"""Find who has the most interests in common with a given user"""
def most_common_interests_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
        )
        
most_common_interests_with["Hero"]
most_common_interests_with[0]
user
users
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]
import matplotlib.pyplot as plt
x, y = zip(*salaries_and_tenures)
plt.plot(x, y)
salaries_and_tenures
"""keys are years, values are lists of the salaries for each tenure"""
salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)
    
"""keys are years, each value is average salary for that tenure"""
salary_by_tenure
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
    }
average_salary_by_tenure
def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"
        
"""keys are tenure buckets, values are lists of salaries for that bucket"""
salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)
    
bucket
salary_by_tenure_bucket[bucket]
""" compute average salary for each group """
"""keys are tenure buckets, values are average salary for that bucket """
average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
    }
average_salary_by_bucket
get_ipython().run_line_magic('save', 'friendship_networks2.py 1-73')
