# A very simple Flask Hello World app for you to get started with...

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "Hello, World!"})


if __name__ == "__main__":
    app.run(debug=True)


@app.route("/")
def hello_world():
    return "Hello from Flask! This will become the spatial job board"
