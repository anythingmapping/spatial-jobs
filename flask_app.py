# A very simple Flask Hello World app for you to get started with...

from flask import jsonify, render_template
from flask_cors import CORS
from flask_migrate import Migrate
from job_listings import create_app
from job_listings.models.models import db

app = create_app()
migrate = Migrate(app, db)
CORS(
    app,
    resources={
        r"/*": {  # Allow all routes
            "origins": [
                "http://localhost:5173",
                "http://localhost:5174",
                "http://localhost:3000",
                "https://anythingmapping.pythonanywhere.com",
            ],
            "methods": ["GET", "POST", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"],
            "expose_headers": ["Content-Range", "X-Content-Range"],
        }
    },
)


# @app.route("/")
# def home():
#     from job_listings.models.models import Job

#     jobs = Job.query.filter_by(status="active").order_by(Job.posted_date.desc()).all()
#     return render_template("index.html", jobs=[job.to_dict() for job in jobs])


@app.route("/")
def stac():
    from job_listings.api.jobs import JOBS

    return render_template("index.html", jobs=JOBS)


# @app.route("/stac")
# def stac():
#     from job_listings.api.jobs import JOBS

#     return render_template("stac.html", jobs=JOBS)


@app.route("/api/jobs")
def get_jobs():
    from job_listings.models.models import Job

    jobs = Job.query.filter_by(status="active").order_by(Job.posted_date.desc()).all()
    return jsonify({"jobs": [job.to_dict() for job in jobs]})


if __name__ == "__main__":
    app.run(debug=True, port=8000)
