# from typing import List, Optional
# from .models import get_conferences, get_users, save_conferences, save_users
# from .schemas import ConferenceCreate, UserCreate

# def create_conference(conference: ConferenceCreate):
#     conferences = get_conferences()
#     conference_id = len(conferences) + 1
#     conference_data = conference.dict()
#     conference_data['id'] = conference_id
    
#     # Convert datetime to string for JSON serialization
#     conference_data['start_time'] = conference_data['start_time'].isoformat()
#     conference_data['end_time'] = conference_data['end_time'].isoformat()
    
#     conferences.append(conference_data)
#     save_conferences(conferences)
#     return conference_data

# def get_conference_by_name(name: str) -> Optional[dict]:
#     conferences = get_conferences()
#     for conference in conferences:
#         if conference['name'] == name:
#             return conference
#     return None

# def create_user(user: UserCreate):
#     users = get_users()
#     user_id = len(users) + 1
#     user_data = user.dict()
#     user_data['id'] = user_id
#     users.append(user_data)
#     save_users(users)
#     return user_data

# def get_user_by_id(user_id: str) -> Optional[dict]:
#     users = get_users()
#     for user in users:
#         if user['user_id'] == user_id:
#             return user
#     return None


from typing import List, Optional
from .models import get_conferences, get_users, get_bookings, save_conferences, save_users, save_bookings
from .schemas import ConferenceCreate, UserCreate, BookingCreate

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

def get_conference_by_id(conference_id: int) -> Optional[dict]:
    conferences = get_conferences()
    for conference in conferences:
        if conference['id'] == conference_id:
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

def create_booking(booking: BookingCreate):
    bookings = get_bookings()
    booking_id = len(bookings) + 1
    booking_data = booking.dict()
    booking_data['id'] = booking_id
    bookings.append(booking_data)
    save_bookings(bookings)
    return booking_data

def get_booking_by_id(booking_id: int) -> Optional[dict]:
    bookings = get_bookings()
    for booking in bookings:
        if booking['id'] == booking_id:
            return booking
    return None

def get_bookings_by_conference(conference_id: int) -> List[dict]:
    bookings = get_bookings()
    return [booking for booking in bookings if booking['conference_id'] == conference_id]

def get_user_bookings(user_id: str) -> List[dict]:
    bookings = get_bookings()
    return [booking for booking in bookings if booking['user_id'] == user_id]
