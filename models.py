from pydantic import BaseModel, validator
import uuid


class Post:
    def __init__(self, author, title, summary, text, time, comments):
        self.author = author
        self.title = title
        self.summary = summary
        self.text = text
        self.time = time
        self.comment = comments
        post_id = str(uuid.uuid4()).split("-")[0]
        self.post_id = post_id


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        user_id = str(uuid.uuid4()).split("-")[0]
        self.user_id = user_id


class Comments:
    def __init__(self, text, time, post_id, user_id):
        self.text = text
        self.time = time
        self.post_id = post_id
        self.user_id = user_id
        comment_id = str(uuid.uuid4()).split("-")[0]
        self.comment_id = comment_id
