# import flask
from application import db


class User(db.Document):
    """The model for holding the User objects in our Mongo DB."""

    user_id = db.IntField(unique=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    email = db.StringField(max_length=40)
    password = db.StringField(max_length=32)


class Course(db.Document):
    """The model for holding the Course objects in our Mongo DB."""

    course_id = db.StringField(max_length=10, unique=True)
    title = db.StringField(max_length=100)
    description = db.StringField(max_length=255)
    credits = db.IntField()
    term = db.StringField(max_length=25)


class Enrollment(db.Document):
    """The model for holding the mapping between Users and Courses."""

    user_id = db.IntField()
    course_id = db.StringField(max_length=10)
