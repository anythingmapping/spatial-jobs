from flask import Blueprint, jsonify, request
from ..models import Job, db
from datetime import datetime

# Create a blueprint for jobs with url_prefix='/api'
jobs_bp = Blueprint("jobs", __name__, url_prefix="/api")


@jobs_bp.route("/jobs", methods=["GET"])
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


@jobs_bp.route("/new", methods=["POST"])
def create_job():
    try:
        data = request.get_json()

        # Create new job
        new_job = Job(
            title=data["title"],
            company=data["company"],
            location=data["location"],
            coordinates=data["coordinates"],  # Expecting [lon, lat]
            description=data["description"],
            remote=data.get("remote", False),
            posted_date=datetime.utcnow(),
            status="active",
        )

        # Add to database
        db.session.add(new_job)
        db.session.commit()

        return (
            jsonify({"message": "Job created successfully", "job": new_job.to_dict()}),
            201,
        )
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to create job", "details": str(e)}), 500


@jobs_bp.route("/jobs/<int:job_id>", methods=["DELETE"])
def delete_job(job_id):
    try:
        job = Job.query.get(job_id)
        if not job:
            return jsonify({"error": "Job not found"}), 404

        db.session.delete(job)
        db.session.commit()

        return jsonify({"message": f"Job {job_id} deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to delete job", "details": str(e)}), 500
