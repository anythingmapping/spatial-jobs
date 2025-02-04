from flask import Blueprint, jsonify, request
from ..models import Job, db

# Create a blueprint for jobs with url_prefix='/api'
jobs_bp = Blueprint("jobs", __name__, url_prefix="/api")


@jobs_bp.route("/jobs")
def get_jobs():
    try:
        # Get all jobs from database
        jobs = Job.query.all()

        # Add debug print to see what's being returned
        print("Found jobs:", jobs)  # Debug line

        # Convert jobs to list of dictionaries
        jobs_list = [job.to_dict() for job in jobs]

        # Add debug print for final response
        response = {"jobs": jobs_list, "total": len(jobs_list)}
        print("Sending response:", response)  # Debug line

        return jsonify(response)
    except Exception as e:
        print("Error:", str(e))  # Debug line
        return jsonify({"error": "Failed to fetch jobs", "details": str(e)}), 500
