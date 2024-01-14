import os


class Config:
    SECRET_KEY = (
        os.environ.get("SECRET_KEY")
        or b"z\xcf4\xb6\x19\xadA\xd8&\xd4\x10\xb2\xf4\xf0T\xcc"
    )
    MONGODB_SETTINGS = {"db": "UTA_Enrollment"}
