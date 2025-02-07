from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .api.jobs import jobs_bp
from .models.models import db
import os
import logging
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()  # Load environment variables


def create_app():
    try:
        app = Flask(__name__)

        # Configuration
        app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

        # Set the instance path explicitly
        instance_path = "/home/anythingmapping/spatial-jobs/instance"

        # Ensure instance directory exists
        os.makedirs(instance_path, exist_ok=True)

        # Use absolute path for database
        app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
            "DATABASE_URL", f"sqlite:///{os.path.join(instance_path, 'jobs.db')}"
        )
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        # Log configuration details
        logger.info(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
        logger.info(f"Instance Path: {instance_path}")
        logger.info(f"Current working directory: {os.getcwd()}")

        # Initialize extensions
        db.init_app(app)

        # Register blueprints
        app.register_blueprint(jobs_bp)

        # Add error handlers
        @app.errorhandler(500)
        def handle_500(error):
            logger.error(f"500 error: {error}")
            return "Internal Server Error", 500

        @app.errorhandler(Exception)
        def handle_exception(error):
            logger.error(f"Unhandled exception: {error}", exc_info=True)
            return "Internal Server Error", 500

        return app

    except Exception as e:
        logger.error(f"Error in create_app: {e}", exc_info=True)
        raise
