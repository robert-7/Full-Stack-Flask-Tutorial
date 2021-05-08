import os

from flask import render_template
from flask import send_from_directory

from application import app


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
def courses():
    """Returns the courses page content."""
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
    print(courseData)
    return render_template("courses.html", courseData=courseData, courses=True)


@app.route("/register")
def register():
    """Returns the registration page content."""
    return render_template("register.html", register=True)


@app.route("/favicon.ico")
def favicon():
    """Sends the favicon.ico file."""
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )
