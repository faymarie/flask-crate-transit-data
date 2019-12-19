import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from transitdata.config import Config
from flask_cors import CORS
from transitdata.config import Config
from transitdata.models import Base
from flask_session import Session

# connect to crateDB 
db = SQLAlchemy()

def create_app(config_class=Config):
    """ Initialize core application. """
    
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app)

    with app.app_context():
        db.init_app(app)
        register_blueprints(app)

    # connct to crate and create tables
    engine = db.create_engine(config_class.SQLALCHEMY_DATABASE_URI, {})
    Base.metadata.create_all(engine)

    return app

def register_blueprints(app):
    from transitdata.main.routes import main
    from transitdata.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(errors)

def start_session(engine):
    connection = engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    return session