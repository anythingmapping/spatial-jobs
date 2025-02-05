from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .api.jobs import jobs_bp
from .models.models import db
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables


def create_app():
    app = Flask(__name__)

    # Configuration
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-key-please-change")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL", "sqlite:///jobs.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(jobs_bp)

    return app
