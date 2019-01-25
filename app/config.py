import os

class Config:
    SECRET_KEY = "any secret string"
    WTF_CSRF_SECRET_KEY = "well things are looing up"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI  = os.getenv('DB_CONNNECTION_STRING')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

