import pytwitter
from process import process_tweet

with open("bearer_token.txt", "r") as file:
    bearer_token = file.readline().strip()

with open("keywords.txt", "r") as file:
    lines = file.readlines()
    keywords = [line.strip() for line in lines]

api = pytwitter.Api(bearer_token=bearer_token)

query_keywords = " OR ".join(keywords)
response = api.search_tweets(query="-is:retweet -is:reply lang:en (%s)" % (query_keywords))

for tweet in response.data:
    process_tweet(tweet)
