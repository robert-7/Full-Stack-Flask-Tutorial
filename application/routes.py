import os

from flask import json
from flask import render_template
from flask import request
from flask import Response
from flask import send_from_directory

from application import app
from application import db

courseData = [
    {
        "courseID": "1111",
        "title": "PHP 101",
        "description": "Intro to PHP",
        "credits": 3,
        "term": "Fall, Spring",
    },
    {
        "courseID": "2222",
        "title": "Java 1",
        "description": "Intro to Java Programming",
        "credits": 4,
        "term": "Spring",
    },
    {
        "courseID": "3333",
        "title": "Adv PHP 201",
        "description": "Advanced PHP Programming",
        "credits": 3,
        "term": "Fall",
    },
    {
        "courseID": "4444",
        "title": "Angular 1",
        "description": "Intro to Angular",
        "credits": 3,
        "term": "Fall, Spring",
    },
    {
        "courseID": "5555",
        "title": "Java 2",
        "description": "Advanced Java Programming",
        "credits": 4,
        "term": "Fall",
    },
]


@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    """Returns the landing page content."""
    return render_template("index.html", index=True)


@app.route("/login")
def login():
    """Returns the login page content."""
    return render_template("login.html", login=True)


@app.route("/courses")
@app.route("/courses/<term>")
def courses(term="Spring 2019"):
    """Returns the courses page content."""
    return render_template(
        "courses.html", courseData=courseData, courses=True, term=term
    )


@app.route("/register")
def register():
    """Returns the registration page content."""
    return render_template("register.html", register=True)


@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    """Returns the enrollment page content."""
    id = request.form.get("courseID")
    title = request.form.get("title")
    term = request.form.get("term")
    return render_template(
        "enrollment.html",
        enrollment=True,
        data={"id": id, "title": title, "term": term},
    )


@app.route("/api")
@app.route("/api/<idx>")
def api(idx=None):
    """Returns the course data as a JSON object."""
    if idx is None:
        jdata = courseData
    else:
        jdata = courseData[int(idx)]
    return Response(json.dumps(jdata), mimetype="application/json")


class User(db.Document):
    """???"""

    user_id = db.IntField(unique=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    email = db.StringField(max_length=40)
    password = db.StringField(max_length=32)


@app.route("/user")
def user():
    """???"""
    # User(
    #     user_id=1,
    #     first_name="Christian",
    #     last_name="Hur",
    #     email="christian@uta.com",
    #     password="abc1234",
    # ).save()
    # User(
    #     user_id=2,
    #     first_name="Mary",
    #     last_name="Jane",
    #     email="mary.jane@uta.com",
    #     password="password123",
    # ).save()
    users = User.objects.all()
    return render_template("user.html", users=users)


@app.route("/favicon.ico")
def favicon():
    """Sends the favicon.ico file."""
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )
