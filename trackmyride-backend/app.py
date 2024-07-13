from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

# Initialize the Flask application
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS)
CORS(app)

# Set up the database URI for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/trackmyride'

# Disable SQLAlchemy event system to save resources
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set the secret key for JWT
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

# Initialize the database object
db = SQLAlchemy(app)

# Initialize database migration management
migrate = Migrate(app, db)

# Initialize the JWT manager
jwt = JWTManager(app)

# Import models
from models import Ride, User

# Import blueprints for routes
from routes.auth import auth_blueprint
from routes.ride import ride_blueprint

# Register blueprints with the application
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(ride_blueprint, url_prefix='/rides')

# Run the application in debug mode
if __name__ == '__main__':
    app.run(debug=True)


