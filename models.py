import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

engine = db.create_engine("")


class Post(Base):

    __tablename__ = "posts"
    post_id = db.Column("id", db.Integer, primary_key=True)
    author = db.Column("author", db.String(50))
    title = db.Column("title", db.String(100))
    summary = db.Column("summary", db.String(250))
    text = db.Column("text", db.String)
    time = db.Column("time", db.Time)

    def __init__(self, author, title, summary, text, time, comments):
        self.author = author
        self.title = title
        self.summary = summary
        self.text = text
        self.time = time
        self.comment = comments
        post_id = str(uuid.uuid4()).split("-")[0]
        self.post_id = post_id


class User(Base):

    __tablename__ = "users"

    user_id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(50))
    email = db.Column("email", db.String(100))
    password = db.Column("password", db.String(250))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        user_id = str(uuid.uuid4()).split("-")[0]
        self.user_id = user_id


class Comments(Base):
    __tablename__ = "comments"

    comment_id = db.Column("id", db.Integer, primary_key=True)
    text = db.Column("text", db.String)
    time = db.Column("time", db.Time)
    post_id = db.Column("post_id", db.String(250))
    user_id = db.Column("user_id", db.String(100))

    def __init__(self, text, time, post_id, user_id):
        self.text = text
        self.time = time
        self.post_id = post_id
        self.user_id = user_id
        comment_id = str(uuid.uuid4()).split("-")[0]
        self.comment_id = comment_id


Session = sessionmaker(bind=engine)
session = Session()
