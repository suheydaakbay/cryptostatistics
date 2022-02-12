class User:
    def __init__(self, user: dict):
        user_metrics = user["public_metrics"]
        followers_count = user_metrics["followers_count"]
        tweet_count = user_metrics["tweet_count"]
        following_count = user_metrics["following_count"]
        username = user["username"]
        verified = user["verified"]

        self.followers_count = followers_count
        self.tweet_count = tweet_count
        self.following_count = following_count
        self.username = username
        self.verified = verified
