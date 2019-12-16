import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'crate://crate@192.168.99.101:4200'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # CRATE_HOST = 'localhost:4200'
    # MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5mb because GIFs are big ;)
    DEBUG = True
    TESTING = False
    # CSRF_ENABLED = True


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