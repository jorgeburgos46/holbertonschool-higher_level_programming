#!/usr/bin/python3
"""Simple API using Flask."""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """Return welcome message."""
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """Return API status."""
    return "OK"


@app.route("/data")
def data():
    """Return list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """Return full user object by username."""
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user to the users dictionary."""
    try:
        user_data = request.get_json(silent=True)
        if user_data is None:
            return jsonify({"error": "Invalid JSON"}), 400
        if "username" not in user_data:
            return jsonify({"error": "Username is required"}), 400
        username = user_data["username"]
        if username in users:
            return jsonify({"error": "Username already exists"}), 409
        users[username] = user_data
        return jsonify({"message": "User added", "user": user_data}), 201
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400


if __name__ == "__main__":
    app.run()