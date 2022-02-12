from stream import TweetStream

with open("bearer_token.txt", "r") as file:
    bearer_token = file.readline().strip()

with open("keywords.txt", "r") as file:
    lines = file.readlines()
    keywords = [line.strip() for line in lines]

stream = TweetStream(bearer_token=bearer_token)

query_keywords = " OR ".join(keywords)
query = f"-is:retweet -is:reply lang:en ({query_keywords})"

stream.manage_rules({
    "add": [
        {"value": query},
    ]
})

stream.search_stream(
    tweet_fields=["created_at", "author_id", "text", "id"],
    place_fields=["country_code"],
    user_fields=["verified","location", "id", "public_metrics"],
    expansions=["author_id", "geo.place_id"],
    return_json=True,
)
