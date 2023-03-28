from fastapi import FastAPI
import models as db

from pydantic import BaseModel

db.Base.metadata.create_all(db.engine)

app = FastAPI()


@app.get("/")
def home():
    our_posts = db.session.query(db.Post).all()
    post = {
        "post_id" : "",
        "author" : "",
        "title": "",
        "text": "",
        "summary" : "",
        "time" : ""
    }
    resault = {
        "number_of_posts" : 0,
        "posts" : []
    }
    for i in our_posts:
        post["post_id"] = i.post_id
        post["author"] = i.poster_id
        post["title"] = i.title
        post["text"] = i.text
        post["summary"] = i.summary
        post["time"] = i.time
        resault["posts"].append(post)
    resault["number_of_posts"] = len(our_posts)
    return resault
