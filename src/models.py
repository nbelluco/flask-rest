import datetime

from src import db


class Plate(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    code = db.Column(db.String(20), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

