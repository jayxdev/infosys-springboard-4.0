# backend/models/patient.py
from backend.db import db

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    room_number = db.Column(db.String(10), nullable=False)
    requests = db.relationship('Request', backref='patient', lazy=True)

    def save(self):
        db.session.add(self)
        db.session.commit()