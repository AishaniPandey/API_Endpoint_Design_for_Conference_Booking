from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from app.crud import create_user, get_user_by_id
from app.schemas import UserCreate

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['POST'])
def add_user():
    try:
        user_data = request.json
        user = UserCreate(**user_data)
        if get_user_by_id(user.user_id):
            return jsonify({"error": "User already exists"}), 400
        created_user = create_user(user)
        return jsonify(created_user), 201
    except ValidationError as e:
        return jsonify(e.errors()), 400
