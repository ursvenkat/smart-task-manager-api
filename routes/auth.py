"""
Authentication Routes

Features:
- Register User
- Login User
- JWT Authentication
"""
from flask import Blueprint, jsonify

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register")
def register():
    return jsonify({
        "message": "User Registration Endpoint"
    })

@auth_bp.route("/login")
def login():
    return jsonify({
        "message": "User Login Endpoint"
    })
