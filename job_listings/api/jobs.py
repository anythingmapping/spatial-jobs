from flask import Blueprint, jsonify

# Create a blueprint for jobs with url_prefix='/api'
jobs_bp = Blueprint("jobs", __name__, url_prefix="/api")

# Sample jobs data - we can move this to a database later
JOBS = [
    {
        "id": 1,
        "title": "GIS Analyst",
        "company": "Spatial Corp",
        "location": "New York, NY",
        "description": "Looking for an experienced GIS analyst...",
        "posted_date": "2024-01-22",
    },
    {
        "id": 2,
        "title": "Remote Sensing Specialist",
        "company": "Earth Data Inc",
        "location": "Remote",
        "description": "Seeking a specialist in satellite imagery analysis...",
        "posted_date": "2024-01-21",
    },
]


@jobs_bp.route("/jobs")
def get_jobs():
    return jsonify({"jobs": JOBS})
