# A very simple Flask Hello World app for you to get started with...

from job_listings import create_app

app = create_app()


@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Spatial Jobs API"})


if __name__ == "__main__":
    app.run(debug=True)
