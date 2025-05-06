from flask import Blueprint, request, jsonify
from backend.models.request import Request  # Use absolute import
from backend.models.patient import Patient  # Use absolute import
from backend.services.speech import transcribe_audio  # Use absolute import
from backend.services.nlp import categorize_request  # Use absolute import

patient_bp = Blueprint('patient', __name__)

@patient_bp.route('/request', methods=['POST'])
def handle_patient_request():
    # Check if the 'audio' file is in the request
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    # Get the audio file and patient_id from the request
    audio_file = request.files['audio']
    patient_id = request.form.get('patient_id')

    # Check if the audio file is empty
    if audio_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Transcribe the audio file
    transcription = transcribe_audio(audio_file)

    # Categorize the request
    category = categorize_request(transcription)

    # Save the request to the database
    new_request = Request(
        content=transcription,
        category=category,
        patient_id=patient_id
    )
    new_request.save()

    return jsonify({"message": "Request received", "category": category}), 201

@patient_bp.route('/requests', methods=['GET'])
def get_patient_requests():
    patient_id = request.args.get('patient_id')
    requests = Request.query.filter_by(patient_id=patient_id).all()
    return jsonify([{
        "id": req.id,
        "content": req.content,
        "category": req.category,
        "status": req.status
    } for req in requests]), 200