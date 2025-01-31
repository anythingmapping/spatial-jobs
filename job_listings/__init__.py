from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .api.jobs import jobs_bp
from .models.models import db


def create_app():
    app = Flask(__name__)

    # Database configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///jobs.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize extensions
    db.init_app(app)

    # Register the jobs blueprint
    app.register_blueprint(jobs_bp)

    return app
