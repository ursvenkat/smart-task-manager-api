"""
Task Management Routes

Features:
- Create Task
- Update Task
- Delete Task
- View Tasks
"""
from flask import Blueprint, jsonify

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/tasks")
def get_tasks():
    return jsonify({
        "message": "List of Tasks"
    })
