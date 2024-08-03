from typing import List, Optional
from .models import get_conferences, get_users, save_conferences, save_users
from .schemas import ConferenceCreate, UserCreate

def create_conference(conference: ConferenceCreate):
    conferences = get_conferences()
    conference_id = len(conferences) + 1
    conference_data = conference.dict()
    conference_data['id'] = conference_id
    
    # Convert datetime to string for JSON serialization
    conference_data['start_time'] = conference_data['start_time'].isoformat()
    conference_data['end_time'] = conference_data['end_time'].isoformat()
    
    conferences.append(conference_data)
    save_conferences(conferences)
    return conference_data

def get_conference_by_name(name: str) -> Optional[dict]:
    conferences = get_conferences()
    for conference in conferences:
        if conference['name'] == name:
            return conference
    return None

def create_user(user: UserCreate):
    users = get_users()
    user_id = len(users) + 1
    user_data = user.dict()
    user_data['id'] = user_id
    users.append(user_data)
    save_users(users)
    return user_data

def get_user_by_id(user_id: str) -> Optional[dict]:
    users = get_users()
    for user in users:
        if user['user_id'] == user_id:
            return user
    return None
