from pytwitter.models import Tweet
from database import save_tweet

def process_tweet(tweet: Tweet):
    save_tweet(id=tweet.id, text=tweet.text)
