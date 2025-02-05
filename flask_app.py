# A very simple Flask Hello World app for you to get started with...

from flask import jsonify, render_template, request, session, redirect, url_for
from flask_cors import CORS
from flask_migrate import Migrate
from job_listings import create_app
from job_listings.models.models import db
import requests
from functools import wraps

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


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)

    return decorated_function


@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")


@app.route("/api/login", methods=["POST"])
def api_login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()
    if user and check_password_hash(user.password_hash, data["password"]):
        session["user_id"] = user.id
        return jsonify({"message": "Login successful"})
    return jsonify({"error": "Invalid username or password"}), 401


@app.route("/", methods=["GET"])
def stac():
    api_url = f"{request.url_root}api/jobs"
    response = requests.get(api_url)
    jobs = response.json()["jobs"]
    return render_template("index.html", jobs=jobs)


@app.route("/api/jobs")
def get_jobs():
    from job_listings.models.models import Job

    jobs = Job.query.filter_by(status="active").order_by(Job.posted_date.desc()).all()
    return jsonify({"jobs": [job.to_dict() for job in jobs]})


@app.route("/new", methods=["GET"])
def new_job_form():
    return render_template("new_job.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
