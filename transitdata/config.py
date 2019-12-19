from os import environ

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'crate://crate@192.168.99.101:4200'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'affiav'
    # CRATE_HOST = 'localhost:4200'
    DEBUG = True
    TESTING = False

    # SECRET_KEY = environ.get('SECRET_KEY')
    # FLASK_APP = environ.get('FLASK_APP')
    # FLASK_ENV = environ.get('FLASK_ENV')


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'crate://crate@192.168.99.101:4200'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'affiav'
    TESTING = True
    DEBUG = True