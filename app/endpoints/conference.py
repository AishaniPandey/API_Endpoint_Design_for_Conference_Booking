from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from app.crud import create_conference, get_conference_by_name
from app.schemas import ConferenceCreate

conference_bp = Blueprint('conference', __name__)

@conference_bp.route('/conferences', methods=['POST'])
def add_conference():
    try:
        conference_data = request.json
        conference = ConferenceCreate(**conference_data)
        if get_conference_by_name(conference.name):
            return jsonify({"error": "Conference already exists"}), 400
        created_conference = create_conference(conference)
        return jsonify(created_conference), 201
    except ValidationError as e:
        return jsonify(e.errors()), 400
