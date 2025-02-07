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
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    # Set the instance path explicitly
    instance_path = "/home/anythingmapping/spatial-jobs/instance"

    # Use absolute path for database
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        # "DATABASE_URL", "sqlite:///jobs.db" local setup
        "DATABASE_URL",
        f"sqlite:///{os.path.join(instance_path, 'jobs.db')}",
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(jobs_bp)

    # For debugging
    print(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
    print(f"Instance Path: {instance_path}")

    return app
