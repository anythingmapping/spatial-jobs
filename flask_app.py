# A very simple Flask Hello World app for you to get started with...

from flask import jsonify
from flask_cors import CORS
from job_listings import create_app

app = create_app()
CORS(
    app,
    origins=[
        "http://localhost:5173",  # Vite's default port
        "http://localhost:3000",  # For local development
        "https://anythingmapping.pythonanywhere.com",  # Your production domain
    ],
)


@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Spatial Jobs API"})


@app.route("/api")
def api_home():
    return jsonify({"message": "Welcome to the Spatial Jobs API"})


if __name__ == "__main__":
    app.run(debug=True, port=8000)
