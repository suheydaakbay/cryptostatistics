from pytwitter.models import Tweet
from database import save_tweet, has_tweet

def process_tweet(tweet: Tweet):
    if not has_tweet(id=tweet.id):
        save_tweet(id=tweet.id, text=tweet.text)
