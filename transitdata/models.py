from flask import current_app
from transitdata import db

class Tile(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        pass