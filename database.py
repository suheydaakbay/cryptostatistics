import sqlite3

con = sqlite3.connect('twitter.sqlite')

cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS tweet (id text PRIMARY KEY, text text)''')
con.commit()

def save_tweet(id: str, text: str):
    cur.execute('''INSERT INTO tweet (id, text) VALUES (?, ?)''', (id, text))
    con.commit()
