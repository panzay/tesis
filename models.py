from datetime import datetime
from app import db


class Transcript(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    timestamp = db.Column(
        db.DateTime,
        default=datetime.now,
        index=True
    )
