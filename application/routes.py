import os

from flask import flash
from flask import json
from flask import redirect
from flask import render_template
from flask import request
from flask import Response
from flask import send_from_directory
from flask import url_for

from application import app
from application.forms import LoginForm
from application.forms import RegisterForm
from application.models import Course  # noqa: F401
from application.models import Enrollment  # noqa: F401
from application.models import User

# TODO: this should be removed, but it's still being read in
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


@app.route("/login", methods=["GET", "POST"])
def login():
    """Returns the login page content."""
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.objects(email=email).first()
        if user and user.get_password(password):
            flash("You are successfully logged in!", "success")
            return redirect("/index")
        else:
            flash("Sorry, something went wrong.", "danger")
    return render_template("login.html", title="Login", form=form, login=True)


@app.route("/courses")
@app.route("/courses/<term>")
def courses(term=None):
    """Returns the courses page content."""
    if term is None:
        term = "Spring 2019"
    # "+courseID" denotes sorting in increasing order by courseID
    classes = Course.objects.order_by("+courseID")
    return render_template("courses.html", courseData=classes, courses=True, term=term)


@app.route("/register", methods=["POST", "GET"])
def register():
    """Returns the registration page content."""
    form = RegisterForm()
    if form.validate_on_submit():
        user_id = User.objects.count()
        app.logger.info("ROBERT - %s - the number of users", user_id)
        user_id += 1
        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        user = User(
            user_id=user_id, email=email, first_name=first_name, last_name=last_name
        )
        user.set_password(password)
        user.save()
        flash("You are successfully registered!", "success")
        return redirect(url_for("index"))
    return render_template("register.html", title="Register", form=form, register=True)


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


# TODO: What is this? Remove this when you're done.
@app.route("/api")
@app.route("/api/<idx>")
def api(idx=None):
    """Returns the course data as a JSON object."""
    if idx is None:
        jdata = courseData
    else:
        jdata = courseData[int(idx)]
    return Response(json.dumps(jdata), mimetype="application/json")


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
