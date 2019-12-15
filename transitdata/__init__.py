import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
# from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, mapper
from sqlalchemy.ext.declarative import declarative_base
from transitdata.config import Config
from flask_cors import CORS
from crate import client


# from flask_restful import Api, Resource
# from flask_restful import reqparse as reqparser


# connection = client.connect("http://192.168.99.101:4200/#!/", username="crate")

# engine = sa.create_engine("crate://localhost:4200/")
# engine = SQLAlchemy()

# create Flask app
def create_app(config_class=Config):
    app = Flask(__name__)
    # basedir = os.path.abspath(os.path.dirname(__file__))
    app.config.from_object(Config)

   # engine to communicate with database
    # db = sa.create_engine('crate://http://192.168.99.101:4200/', username="crate")

    # create a session for the database engine 
    # Session = sessionmaker(bind=db)
    # session = Session() 

    # map tables to classes
    Base = declarative_base() 

    # db.init_app(app)
    # create db tables 
    # db.create_all()
    #  object container that containing table attributes 
    # metadata = MetaData(db)
    
    # apply CORS headers to all responses
    CORS(app)


    # # register app packages
    # with app.app_context():
    #     from . import routes
    #     app.register_blueprint(routes.bp)

    from transitdata.main.routes import main
    from transitdata.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app