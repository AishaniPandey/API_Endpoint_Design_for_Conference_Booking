from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from app.crud import create_conference, get_conference_by_name
from app.schemas import ConferenceCreate
from app.crud import get_conferences, get_user_by_id

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
    
@conference_bp.route('/conferences/search', methods=['GET'])
def search_conferences():
    location = request.args.get('location')
    topic = request.args.get('topic')
    name = request.args.get('name')
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')

    conferences = get_conferences()
    result = conferences

    if location:
        result = [c for c in result if c['location'] == location]
    if topic:
        result = [c for c in result if topic in c['topics']]
    if name:
        result = [c for c in result if name.lower() in c['name'].lower()]
    if start_time:
        result = [c for c in result if c['start_time'] >= start_time]
    if end_time:
        result = [c for c in result if c['end_time'] <= end_time]

    return jsonify(result), 200

@conference_bp.route('/conferences/suggested/<string:user_id>', methods=['GET'])
def suggested_conferences(user_id: str):
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    interested_topics = user['interested_topics']
    conferences = get_conferences()
    suggested = [c for c in conferences if any(topic in c['topics'] for topic in interested_topics)]

    return jsonify(suggested[:10]), 200
