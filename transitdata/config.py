import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("DEV_SECRET_KEY")
    TESTING = False
    DEBUG = True

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("TEST_SECRET_KEY")
    TESTING = True
    DEBUG = True