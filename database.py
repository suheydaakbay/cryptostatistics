from datetime import datetime
import sqlite3

from tweet import Tweet

con = sqlite3.connect('twitter.sqlite')

cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS tweet (
    id text PRIMARY KEY,
    text text,
    created_at integer,
    author_id integer,
    author_verified integer,
    author_followers integer,
    author_followings integer,
    author_tweets integer
)''')
con.commit()

def save_tweet(tweet: Tweet):
    cur.execute('''INSERT INTO tweet (
        id,
        text,
        created_at,
        author_id,
        author_verified,
        author_followers,
        author_followings,
        author_tweets
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (
        tweet.id,
        tweet.text,
        tweet.created_at,
        tweet.author_id,
        tweet.author.verified,
        tweet.author.followers_count,
        tweet.author.following_count,
        tweet.author.tweet_count,
    ))
    con.commit()
