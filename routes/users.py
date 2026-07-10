"""
User Management Routes

Features:
- View Users
- Update User
- Delete User
"""
from flask import Blueprint, jsonify

user_bp = Blueprint("users", __name__)

@user_bp.route("/users")
def get_users():
    return jsonify({
        "message": "List of Users"
    })
