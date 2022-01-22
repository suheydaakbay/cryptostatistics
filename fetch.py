from nbformat import read
import pytwitter

with open("bearer_token.txt", "r") as file:
    bearer_token = file.readline()

api = pytwitter.Api(bearer_token=bearer_token)

query = api.search_tweets(query="lang:en (btc OR eth)")

for tweet in query.data:
    print("---")
    print(tweet.text)
