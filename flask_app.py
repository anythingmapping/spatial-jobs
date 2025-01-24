# A very simple Flask Hello World app for you to get started with...

from flask import jsonify
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
    return jsonify({"message": "Welcome to the Spatial Jobs API"})


@app.route("/api")
def api_home():
    return jsonify({"message": "Welcome to the Spatial Jobs API"})


if __name__ == "__main__":
    app.run(debug=True, port=8000)
