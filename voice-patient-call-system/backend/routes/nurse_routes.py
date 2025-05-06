from flask import Blueprint, request, jsonify
from backend.models.request import Request
from backend.models.nurse import Nurse
from backend.services.escalation import escalate_request

nurse_bp = Blueprint('nurse', __name__)

@nurse_bp.route('/requests', methods=['GET'])
def get_requests():
    nurse_id = request.args.get('nurse_id')
    requests = Request.query.filter_by(nurse_id=nurse_id).all()
    return jsonify([{
        "id": req.id,
        "content": req.content,
        "category": req.category,
        "status": req.status,
        "patient_id": req.patient_id
    } for req in requests]), 200

@nurse_bp.route('/complete-request', methods=['POST'])
def complete_request():
    request_id = request.json.get('request_id')
    req = Request.query.get(request_id)
    if not req:
        return jsonify({"message": "Request not found"}), 404

    req.status = "Completed"
    req.save()
    return jsonify({"message": "Request marked as completed"}), 200