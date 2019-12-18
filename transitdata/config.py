from os import environ

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'crate://crate@192.168.99.101:4200'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'affiav'
    # CRATE_HOST = 'localhost:4200'
    # MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5mb because GIFs are big ;)
    DEBUG = True
    TESTING = False
    # CSRF_ENABLED = True
        # General Config
    # SECRET_KEY = environ.get('SECRET_KEY')
    # FLASK_APP = environ.get('FLASK_APP')
    # FLASK_ENV = environ.get('FLASK_ENV')


class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URI = 'crate://crate@localhost:4200'


# class StagingConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True


# class DevelopmentConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True


# class TestingConfig(Config):
#     TESTING = True