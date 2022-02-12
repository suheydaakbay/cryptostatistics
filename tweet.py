import dateutil.parser
from user import User

class Tweet:
    def __init__(self, tweet: dict):
        data = tweet["data"]
        includes = tweet["includes"]

        id = data["id"]
        author_id = data["author_id"]
        created_at = data["created_at"]
        text = data["text"]

        users = includes["users"]
        for user in users:
            if user["id"] == author_id:
                author = user
                break

        author = User(author)

        self.id = id
        self.author_id = author_id
        self.created_at = dateutil.parser.parse(created_at)
        self.text = text
        self.author = author
