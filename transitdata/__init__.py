import os
from flask import Flask
import sqlalchemy as sa
# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker, mapper
from sqlalchemy.ext.declarative import declarative_base
from transitdata.config import Config
from flask_cors import CORS
# from crate import client
from sqlalchemy.ext.declarative import declarative_base
from transitdata.config import Config
from transitdata.models import Base

def create_app(config_class=Config):
    """ Initialize core application. """
    
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # connect to crateDB 
    engine = sa.create_engine(Config.SQLALCHEMY_DATABASE_URI)
    
    # create tables
    Base.metadata.create_all(engine)

    # register blueprints
    
    from transitdata.main.routes import main
    from transitdata.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app