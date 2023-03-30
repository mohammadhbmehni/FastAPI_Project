from fastapi import FastAPI,Request,HTTPException
import models as db
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

templates = Jinja2Templates(directory=r".\Front")


db.Base.metadata.create_all(db.engine)

app = FastAPI()
app.mount("/Front/css", StaticFiles(directory="Front"), name="Front")

curren_user = {
    "logged_in" : False,
    "user_id": "",
    "name" : "",
    "current_post_looking" : ""
}


class Register(BaseModel):
    name : str
    email : str
    password: str
    second_password : str


@app.get("/")
def home(request : Request):
    our_posts = db.session.query(db.Post).all()

    resault = {
        "number_of_posts" : 0,
        "posts" : []
    }
    for i in our_posts:
        post = {
            "post_id": "",
            "author": "",
            "title": "",
            "text": "",
            "summary": "",
            "time": "",
            "comments_count": 0
        }
        our_user = db.session.query(db.User).filter(db.User.user_id == i.poster_id).one()
        our_comments = db.session.query(db.Comments).filter(db.Comments.post_id == i.post_id).all()
        post["post_id"] = i.post_id
        post["author"] = our_user.name
        post["title"] = i.title
        post["text"] = i.text
        post["summary"] = i.summary
        post["time"] = i.time
        post["comments_count"] = len(our_comments)
        resault["posts"].append(post)
    resault["number_of_posts"] = len(our_posts)
    return templates.TemplateResponse("index.html", {"request":request,"resault":resault})

@app.get("/post/{post_id}")
def show_post(request : Request, post_id):
    our_post = db.session.query(db.Post).filter(db.Post.post_id == post_id).one()
    our_user = db.session.query(db.User).filter(db.User.user_id == our_post.poster_id).one()
    our_comments = db.session.query(db.Comments).filter(db.Comments.post_id == our_post.post_id)

    resault = {
        "post": {
            "post_id": our_post.post_id,
            "author": our_user.name,
            "title": our_post.title,
            "text": our_post.text,
            "summary": our_post.summary,
            "time": our_post.time
        },
        "comments" : [],
        "other_posts": []
    }
    for i in our_comments:
        our_user = db.session.query(db.User).filter(db.User.user_id == i.user_id).one()
        comment_schema = {"comment_id": i.comment_id, "user_id": i.user_id,"user_name" :our_user.name,"post_id": i.post_id, "text": i.text,
                          "time": i.time}
        resault["comments"].append(comment_schema)
    other_posts = db.session.query(db.Post).filter(db.Post.post_id != post_id).limit(3).all()
    for post in other_posts:
        our_comments = db.session.query(db.Comments).filter(db.Comments.post_id == post.post_id).all()
        our_user = db.session.query(db.User).filter(db.User.user_id == post.poster_id).one()
        other_post = {
            "post_id": post.post_id,
            "author": our_user.name,
            "title": post.title,
            "text": post.text,
            "summary": post.summary,
            "time": post.time,
            "comments_count": len(our_comments)
        }
        resault["other_posts"].append(other_post)

    return templates.TemplateResponse("post.html", {"request":request,"resault":resault})


@app.get("/about")
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request":request})


@app.get("/contact")
def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request":request})


@app.post("/register")
def register(register_req : Register):
    our_user = db.session.query(db.User).all()
    for user in our_user:
        if user.name == register_req.name or user.email == register_req.email:
            raise HTTPException(detail="user already exists",status_code=409)
    if register_req.password != register_req.second_password:
        raise HTTPException(status_code=401,detail="passwords didn't matched")
    if len(register_req.password) <8 :
        raise HTTPException(status_code=401,detail="password is too short")
    if len(register_req.name) < 3 :
        raise HTTPException(status_code=401,detail="username is too short")
    register_response = {
        "is_registered":"ok"
    }
    new_user = db.User(register_req.name,register_req.email,register_req.password)
    db.session.add(new_user)
    db.session.commit()
    return register_response


@app.get("/log-in")
def login_page(request:Request):
    return templates.TemplateResponse("login.html", {"request":request})