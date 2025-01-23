# A very simple Flask Hello World app for you to get started with...

from flask import jsonify, redirect
from flask_cors import CORS
from job_listings import create_app

app = create_app()
CORS(
    app,
    origins=[
        "http://localhost:5173",  # Vite's default port
        "http://localhost:3000",  # For local development
        "https://anythingmapping.pythonanywhere.com",  # Your production domain
        "https://spatial-jobs.vercel.app",  # If you deploy frontend to Vercel
    ],
)


@app.route("/")
def home():
    # In production, we'll just return the API welcome message
    # since the frontend will be hosted separately
    return jsonify({"message": "Welcome to the Spatial Jobs API"})


@app.route("/api")
def api_home():
    return jsonify({"message": "Welcome to the Spatial Jobs API"})


if __name__ == "__main__":
    app.run(debug=True, port=8000)
