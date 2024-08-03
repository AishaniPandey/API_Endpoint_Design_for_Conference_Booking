# from flask import Flask
# from app.endpoints.conference import conference_bp
# from app.endpoints.user import user_bp

# app = Flask(__name__)

# app.register_blueprint(conference_bp, url_prefix='/api/v1')
# app.register_blueprint(user_bp, url_prefix='/api/v1')

# @app.route('/')
# def home():
#     return "Conference Booking API"

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask
from app.endpoints.conference import conference_bp
from app.endpoints.user import user_bp
from app.endpoints.booking import booking_bp

app = Flask(__name__)

app.register_blueprint(conference_bp, url_prefix='/api/v1')
app.register_blueprint(user_bp, url_prefix='/api/v1')
app.register_blueprint(booking_bp, url_prefix='/api/v1')

@app.route('/')
def home():
    return "Conference Booking API"

if __name__ == '__main__':
    app.run(debug=True)
