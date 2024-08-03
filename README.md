# Conference Booking API

## Description

This project is a Conference Booking API built with Flask. It allows users to book conferences, manage bookings, and handle waitlisting scenarios. The API provides endpoints for creating users, creating conferences, booking conferences, and managing bookings.

## Features

- User registration
- Conference creation
- Booking conferences
- Waitlisting if the conference is full
- Automatically promote waitlisted bookings if a slot becomes available
- Search for conferences

## Installation

To get started with this project, follow the steps below:

### Prerequisites

- Python 3.7+
- Pip (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/yourusername/conference-booking-api.git
cd conference-booking-api
```

### Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

```
### Install Dependencies

## Usage

### Run the Application
```bash
python -m app.main

```
The API will be available at http://127.0.0.1:5000.

## API Endpoints

### Users

Create User
URL: /api/v1/users
Method: POST

### Conference

Create Conference
URL: /api/v1/conferences
Method: POST

### Booking

- Create Booking,
URL: /api/v1/bookings,
Method: POST

- Get Booking Status,
URL: /api/v1/bookings/<booking_id>,
Method: GET

- Confirm Waitlist Booking,
URL: /api/v1/bookings/confirm_waitlist/<booking_id>,
Method: POST

-Cancel Booking,
URL: /api/v1/bookings/<booking_id>,
Method: DELETE
