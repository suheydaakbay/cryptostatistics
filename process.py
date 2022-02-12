from typing import Dict, List
from database import save_tweet
from tweet import Tweet

def process_tweet(tweet: dict):
    print(tweet)
    print()
    tweet = Tweet(tweet)

    save_tweet(tweet)
