from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restx import Api

from config import Config

# initiate the main web app
app = Flask(__name__)
app.config.from_object(Config)

# initiate the mongo engine
db = MongoEngine()
db.init_app(app)

# initiate the API
api = Api()
api.init_app(app)

from application import routes  # noqa: E402,F401
