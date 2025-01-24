# A very simple Flask Hello World app for you to get started with...

from flask import jsonify, render_template
from flask_cors import CORS
from job_listings import create_app

app = create_app()
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


@app.route("/")
def home():
    from job_listings.api.jobs import JOBS

    return render_template("index.html", jobs=JOBS)


@app.route("/api/jobs")
def get_jobs():
    from job_listings.api.jobs import JOBS

    return jsonify({"jobs": JOBS})


if __name__ == "__main__":
    app.run(debug=True, port=8000)
