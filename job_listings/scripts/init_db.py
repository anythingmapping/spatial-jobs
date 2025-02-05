import os
import sys
from datetime import datetime
from werkzeug.security import generate_password_hash

# Add the project root directory to Python path
project_root = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
sys.path.append(project_root)

from flask import Flask
from job_listings.models.models import db, User, Job
from dotenv import load_dotenv

load_dotenv()


def init_db():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("PROD_DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        # Create all tables
        db.create_all()

        # Create admin user if it doesn't exist
        admin = User.query.filter_by(username=os.getenv("ADMIN_USERNAME")).first()
        if not admin:
            admin = User(
                username=os.getenv("ADMIN_USERNAME"),
                password_hash=generate_password_hash(os.getenv("ADMIN_PASSWORD")),
                email=os.getenv("ADMIN_EMAIL"),
            )
            db.session.add(admin)
            db.session.commit()
            print("Admin user created successfully")

        print("Database initialized successfully")


if __name__ == "__main__":
    init_db()
