from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    coordinates = db.Column(db.JSON)  # Store [lon, lat]
    description = db.Column(db.Text, nullable=False)
    remote = db.Column(db.Boolean, default=False)
    posted_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default="active")  # active, filled, expired
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "company": self.company,
            "location": self.location,
            "coordinates": self.coordinates,
            "description": self.description,
            "remote": self.remote,
            "posted_date": self.posted_date.strftime("%Y-%m-%d"),
            "status": self.status,
        }
