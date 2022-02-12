import pytwitter

from process import process_tweet

class TweetStream(pytwitter.StreamApi):
    def on_tweet(self, tweet: dict):
        process_tweet(tweet)
