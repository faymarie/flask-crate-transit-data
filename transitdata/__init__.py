import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS
from transitdata.config import Config
from transitdata.models import Base


db = SQLAlchemy()

def create_app(config_class=Config):
    """ Initialize core application. """
    
    app = Flask(__name__)
    app.config.from_object(config_class)
    # CORS(app)

    with app.app_context():
        db.init_app(app)
        register_blueprints(app)

    # connect to crateDB and create tables
    engine = db.create_engine(config_class.SQLALCHEMY_DATABASE_URI, {})
    Base.metadata.create_all(engine)

    return app

def register_blueprints(app):
    from transitdata.main.routes import main
    from transitdata.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(errors)