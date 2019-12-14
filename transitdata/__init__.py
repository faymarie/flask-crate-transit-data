from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from transitdata.config import Config

# from flask_restful import Api, Resource
# from flask_restful import reqparse as reqparser
# from flask_cors import CORS

# from crate.client import connect

# connection = client.connect("http://localhost:4200/", username="crate")

db = SQLAlchemy()

# create Flask app
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from transitdata.main.routes import main
    from transitdata.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(errors)
   # apply CORS headers to all responses
    # CORS(app)

    return app