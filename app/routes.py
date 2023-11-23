from flask import jsonify, request, abort
from app import app
from app.models import Task

tasks = []

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks:" [task.__dict__ for task in tasks]})

