# from flask import Blueprint, request, jsonify
# from pydantic import ValidationError
# from app.crud import create_booking, get_conference_by_id, get_user_by_id, get_bookings_by_conference, get_user_bookings, get_booking_by_id, get_bookings, save_bookings
# from app.schemas import BookingCreate

# booking_bp = Blueprint('booking', __name__)

# @booking_bp.route('/bookings', methods=['POST'])
# def book_conference():
#     try:
#         booking_data = request.json
#         booking = BookingCreate(**booking_data)
        
#         conference = get_conference_by_id(booking.conference_id)
#         if not conference:
#             return jsonify({"error": "Conference not found"}), 404
        
#         user = get_user_by_id(booking.user_id)
#         if not user:
#             return jsonify({"error": "User not found"}), 404

#         user_bookings = get_user_bookings(booking.user_id)
#         for b in user_bookings:
#             existing_conference = get_conference_by_id(b['conference_id'])
#             if existing_conference and existing_conference['start_time'] < conference['end_time'] and existing_conference['end_time'] > conference['start_time']:
#                 return jsonify({"error": "User already has a booking that overlaps with this conference"}), 400

#         bookings = get_bookings_by_conference(booking.conference_id)
#         confirmed_bookings = [b for b in bookings if b['status'] == 'confirmed']

#         if len(confirmed_bookings) < conference['available_slots']:
#             booking.status = 'confirmed'
#         else:
#             booking.status = 'waitlisted'
        
#         created_booking = create_booking(booking)
#         return jsonify(created_booking), 201
#     except ValidationError as e:
#         return jsonify(e.errors()), 400

# @booking_bp.route('/bookings/<int:booking_id>', methods=['GET'])
# def get_booking_status(booking_id: int):
#     booking = get_booking_by_id(booking_id)
#     if not booking:
#         return jsonify({"error": "Booking not found"}), 404
#     return jsonify(booking), 200

# @booking_bp.route('/bookings/confirm_waitlist/<int:booking_id>', methods=['POST'])
# def confirm_waitlist_booking(booking_id: int):
#     booking = get_booking_by_id(booking_id)
#     if not booking:
#         return jsonify({"error": "Booking not found"}), 404

#     if booking['status'] != 'waitlisted':
#         return jsonify({"error": "Booking is not waitlisted"}), 400

#     conference = get_conference_by_id(booking['conference_id'])
#     if not conference:
#         return jsonify({"error": "Conference not found"}), 404

#     bookings = get_bookings_by_conference(booking['conference_id'])
#     confirmed_bookings = [b for b in bookings if b['status'] == 'confirmed']

#     if len(confirmed_bookings) < conference['available_slots']:
#         booking['status'] = 'confirmed'
#         save_bookings(bookings)
#         return jsonify(booking), 200
#     else:
#         return jsonify({"error": "No available slots to confirm booking"}), 400

# @booking_bp.route('/bookings/<int:booking_id>', methods=['DELETE'])
# def cancel_booking(booking_id: int):
#     booking = get_booking_by_id(booking_id)
#     if not booking:
#         return jsonify({"error": "Booking not found"}), 404

#     bookings = get_bookings()
#     bookings = [b for b in bookings if b['id'] != booking_id]

#     if booking['status'] == 'confirmed':
#         conference_bookings = get_bookings_by_conference(booking['conference_id'])
#         waitlisted_bookings = [b for b in conference_bookings if b['status'] == 'waitlisted']
#         if waitlisted_bookings:
#             waitlisted_bookings[0]['status'] = 'confirmed'
    
#     save_bookings(bookings)
#     return jsonify({"message": "Booking canceled"}), 200


from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from app.crud import create_booking, get_conference_by_id, get_user_by_id, get_bookings_by_conference, get_user_bookings, get_booking_by_id, get_bookings, save_bookings
from app.schemas import BookingCreate
import logging

logging.basicConfig(level=logging.INFO)

booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/bookings', methods=['POST'])
def book_conference():
    try:
        booking_data = request.json
        booking = BookingCreate(**booking_data)
        
        conference = get_conference_by_id(booking.conference_id)
        if not conference:
            return jsonify({"error": "Conference not found"}), 404
        
        user = get_user_by_id(booking.user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        user_bookings = get_user_bookings(booking.user_id)
        for b in user_bookings:
            existing_conference = get_conference_by_id(b['conference_id'])
            if existing_conference and existing_conference['start_time'] < conference['end_time'] and existing_conference['end_time'] > conference['start_time']:
                return jsonify({"error": "User already has a booking that overlaps with this conference"}), 400

        bookings = get_bookings_by_conference(booking.conference_id)
        confirmed_bookings = [b for b in bookings if b['status'] == 'confirmed']

        if len(confirmed_bookings) < conference['available_slots']:
            booking.status = 'confirmed'
        else:
            booking.status = 'waitlisted'
        
        created_booking = create_booking(booking)
        return jsonify(created_booking), 201
    except ValidationError as e:
        return jsonify(e.errors()), 400

@booking_bp.route('/bookings/<int:booking_id>', methods=['GET'])
def get_booking_status(booking_id: int):
    booking = get_booking_by_id(booking_id)
    if not booking:
        return jsonify({"error": "Booking not found"}), 404
    return jsonify(booking), 200

@booking_bp.route('/bookings/confirm_waitlist/<int:booking_id>', methods=['POST'])
def confirm_waitlist_booking(booking_id: int):
    booking = get_booking_by_id(booking_id)
    if not booking:
        return jsonify({"error": "Booking not found"}), 404

    if booking['status'] != 'waitlisted':
        return jsonify({"error": "Booking is not waitlisted"}), 400

    conference = get_conference_by_id(booking['conference_id'])
    if not conference:
        return jsonify({"error": "Conference not found"}), 404

    bookings = get_bookings_by_conference(booking['conference_id'])
    confirmed_bookings = [b for b in bookings if b['status'] == 'confirmed']

    if len(confirmed_bookings) < conference['available_slots']:
        booking['status'] = 'confirmed'
        save_bookings(bookings)
        return jsonify(booking), 200
    else:
        return jsonify({"error": "No available slots to confirm booking"}), 400

@booking_bp.route('/bookings/<int:booking_id>', methods=['DELETE'])
def cancel_booking(booking_id: int):
    booking = get_booking_by_id(booking_id)
    if not booking:
        return jsonify({"error": "Booking not found"}), 404

    bookings = get_bookings()
    updated_bookings = [b for b in bookings if b['id'] != booking_id]

    if booking['status'] == 'confirmed':
        conference_bookings = get_bookings_by_conference(booking['conference_id'])
        waitlisted_bookings = [b for b in conference_bookings if b['status'] == 'waitlisted']
        if waitlisted_bookings:
            waitlisted_bookings[0]['status'] = 'confirmed'
            updated_bookings.append(waitlisted_bookings[0])
    
    save_bookings(updated_bookings)
    return jsonify({"message": "Booking canceled"}), 200
