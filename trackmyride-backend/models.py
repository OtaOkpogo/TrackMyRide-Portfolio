from app import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# User model
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    
    # Define relationship to Ride
    rides = relationship('Ride', backref='user', lazy=True)

# Ride model
class Ride(db.Model):
    __tablename__ = 'rides'
    id = Column(Integer, primary_key=True)
    origin = Column(String(200), nullable=False)
    destination = Column(String(200), nullable=False)
    date = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

