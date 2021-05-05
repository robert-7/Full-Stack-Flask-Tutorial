import os
from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route("/")
def index():
    """Sends a default message for hitting the root endpoint."""
    return "<h1>Hello Earth!!!</h1>"


@app.route("/favicon.ico")
def favicon():
    """Sends the favicon"""
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )
