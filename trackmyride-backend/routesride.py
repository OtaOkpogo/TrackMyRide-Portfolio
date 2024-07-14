from flask import Blueprint, request, jsonify
from app import db
from models import Ride
from flask_jwt_extended import jwt_required, get_jwt_identity

# Create a blueprint for ride routes
ride_blueprint = Blueprint('ride', __name__)

# Create a new ride route
@ride_blueprint.route('/create', methods=['POST'])
@jwt_required()
def create_ride():
    data = request.get_json()
    origin = data.get('origin')
    destination = data.get('destination')
    date = data.get('date')
    current_user = get_jwt_identity()
    user_id = User.query.filter_by(username=current_user['username']).first().id

    # Create a new ride instance
    new_ride = Ride(origin=origin, destination=destination, date=date, user_id=user_id)

    # Add the ride to the database
    db.session.add(new_ride)
    db.session.commit()

    return jsonify({"message": "Ride created successfully"}), 201

# Get all rides route
@ride_blueprint.route('/', methods=['GET'])
def get_rides():
    rides = Ride.query.all()
    result = []
    for ride in rides:
        ride_data = {
            'id': ride.id,
            'origin': ride.origin,
            'destination': ride.destination,
            'date': ride.date,
            'user_id': ride.user_id
        }
        result.append(ride_data)
    return jsonify(result), 200

