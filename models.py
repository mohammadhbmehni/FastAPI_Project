import sqlalchemy as db
from sqlalchemy.orm import sessionmaker,declarative_base
import uuid
from datetime import datetime


Base = declarative_base()
            #   "postgresql+psycopg2://username:password@localhost:5432/database_name"
DATABASE_URL = "postgresql+psycopg2://postgres:1379@localhost:5432/postgres"

engine = db.create_engine(DATABASE_URL)


class User(Base):

    __tablename__ = "users"

    user_id = db.Column("user_id", db.String(20), primary_key=True)
    name = db.Column("name", db.String(50))
    email = db.Column("email", db.String(100))
    password = db.Column("password", db.String(250))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        user_id = str(uuid.uuid4()).split("-")[0]
        self.user_id = user_id


class Post(Base):

    __tablename__ = "posts"
    post_id = db.Column("post_id", db.Integer, primary_key=True)
    poster_id = db.Column("poster_id",db.String(50))
    #author = db.Column("author", db.String(50))
    title = db.Column("title", db.String(100))
    summary = db.Column("summary", db.String(250))
    text = db.Column("text", db.String)
    time = db.Column("time", db.Time)

    def __init__(self, author, title, text):
        self.poster_id = author
        self.title = title
        self.text = text
        if len(text) > 250:
            summary = text[:250]
        else:
            summary = text
        self.summary = summary
        now = datetime.now()
        time = now.strftime("%Y-%m-%d")
        self.time = time
        post_id = str(uuid.uuid4()).split("-")[0]
        self.post_id = post_id


class Comments(Base):
    __tablename__ = "comments"

    comment_id = db.Column("comment_id", db.Integer, primary_key=True,index=True)
    text = db.Column("text", db.String)
    time = db.Column("time", db.Time)
    post_id = db.Column("post_id",db.ForeignKey("posts.post_id"))
    #post_id = db.Column("post_id", db.String(250))
    user_id = db.Column("user_id",db.ForeignKey("users.user_id"))
    #user_id = db.Column("user_id", db.String(100))

    def __init__(self, text, post_id, user_id):
        self.text = text
        now = datetime.now()
        time = now.strftime("%Y-%m-%d")
        self.time = time
        self.post_id = post_id
        self.user_id = user_id
        comment_id = str(uuid.uuid4()).split("-")[0]
        self.comment_id = comment_id


Session = sessionmaker(bind=engine)
session = Session()