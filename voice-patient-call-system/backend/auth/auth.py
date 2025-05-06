from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from models.patient import Patient
from models.nurse import Nurse

def signup_patient():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_patient = Patient(
        username=data['username'],
        password=hashed_password,
        room_number=data['room_number']
    )
    new_patient.save()
    return jsonify({"message": "Patient registered successfully"}), 201

def login_patient():
    data = request.get_json()
    patient = Patient.query.filter_by(username=data['username']).first()
    if patient and check_password_hash(patient.password, data['password']):
        return jsonify({"message": "Login successful", "patient_id": patient.id}), 200
    return jsonify({"message": "Invalid credentials"}), 401

def login_nurse():
    data = request.get_json()
    nurse = Nurse.query.filter_by(username=data['username']).first()
    if nurse and check_password_hash(nurse.password, data['password']):
        return jsonify({"message": "Login successful", "nurse_id": nurse.id}), 200
    return jsonify({"message": "Invalid credentials"}), 401