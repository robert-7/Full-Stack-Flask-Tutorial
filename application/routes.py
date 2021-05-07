import os

from flask import render_template
from flask import send_from_directory

from application import app


@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    """Sends a default message for hitting the root endpoint."""
    return render_template("index.html", login=True)


@app.route("/login")
def login():
    """Sends a default message for hitting the root endpoint."""
    return render_template("login.html")


@app.route("/courses")
def courses():
    """Sends a default message for hitting the root endpoint."""
    return render_template("courses.html")


@app.route("/register")
def register():
    """Sends a default message for hitting the root endpoint."""
    return render_template("register.html")


@app.route("/favicon.ico")
def favicon():
    """Sends the favicon.ico file."""
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )