from flask import jsonify
from app import app

# Sample jobs data
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


@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Spatial Jobs API"})


@app.route("/api/jobs")
def get_jobs():
    return jsonify({"jobs": JOBS})
