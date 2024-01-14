import os

from flask import flash
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import session
from flask import url_for
from flask_restx import Resource

from application import api
from application import app
from application.forms import LoginForm
from application.forms import RegisterForm
from application.models import Course  # noqa: F401
from application.models import Enrollment  # noqa: F401
from application.models import User

# TODO: We should be using global strings within flash() functions

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


###################################################


@api.route("/api", "/api/")
class GetAndPost(Resource):

    # GET all
    def get(self):
        return jsonify(User.objects.all())

    # POST all
    def post(self):
        data = api.payload
        user = User(
            user_id=data["user_id"],
            email=data["email"],
            first_name=data["first_name"],
            last_name=data["last_name"],
        )
        # TODO: This is insecure. We should check to see if the user exists before
        # trying to create them.
        user.set_password(data["password"])
        user.save()
        return jsonify(User.objects(user_id=data["user_id"]))


@api.route("/api/<idx>")
class GetUpdateDelete(Resource):

    # GET one
    def get(self, idx):
        return jsonify(User.objects(user_id=idx))

    # PUT one
    def put(self, idx):
        data = api.payload
        user = User.objects(user_id=idx)
        user.update(**data)
        return jsonify(User.objects(user_id=idx))

    # DELETE one
    def delete(self, idx):
        user = User.objects(user_id=idx)
        user.delete()
        return jsonify("User is deleted!")


###################################################


@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    """Returns the landing page content."""
    return render_template("index.html", index=True)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Returns the login page content."""
    if session.get("username"):
        return redirect(url_for("index"))

    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.objects(email=email).first()
        if user and user.get_password(password):
            flash("You are successfully logged in!", "success")
            session["user_id"] = user.user_id
            session["username"] = user.first_name
            return redirect("/index")
        else:
            flash("Sorry, something went wrong.", "danger")
    return render_template("login.html", title="Login", form=form, login=True)


@app.route("/logout")
def logout():
    session["user_id"] = False
    session.pop("username", None)
    return redirect(url_for("index"))


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
    if session.get("username"):
        return redirect(url_for("index"))
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
    if not session.get("username"):
        return redirect(url_for("login"))

    courseID = request.form.get("courseID")
    courseTitle = request.form.get("title")
    user_id = session.get("user_id")

    # we check if we're coming from the course page here
    # if there's a courseID, it means we're enrolling in a course
    if courseID:
        if Enrollment.objects(user_id=user_id, courseID=courseID):
            flash(
                f"Oops! You are already registered in course {courseTitle}!",
                "danger",
            )
            return redirect(url_for("courses"))
        else:
            enrollment = Enrollment(user_id=user_id, courseID=courseID)
            enrollment.save()
            flash(f"You are enrolled in {courseTitle}!", "success")

    classes = list(
        User.objects.aggregate(
            *[
                {
                    "$lookup": {
                        "from": "enrollment",
                        "localField": "user_id",
                        "foreignField": "user_id",
                        "as": "r1",
                    }
                },
                {
                    "$unwind": {
                        "path": "$r1",
                        "includeArrayIndex": "r1_id",
                        "preserveNullAndEmptyArrays": False,
                    }
                },
                {
                    "$lookup": {
                        "from": "course",
                        "localField": "r1.courseID",
                        "foreignField": "courseID",
                        "as": "r2",
                    }
                },
                {"$unwind": {"path": "$r2", "preserveNullAndEmptyArrays": False}},
                {"$match": {"user_id": user_id}},
                {"$sort": {"courseID": 1}},
            ]
        )
    )

    return render_template(
        "enrollment.html",
        enrollment=True,
        title="Enrollment",
        classes=classes,
    )


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
