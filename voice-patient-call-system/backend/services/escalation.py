from backend.models.request import Request
from backend.models.nurse import Nurse

def escalate_request(request_id):
    request = Request.query.get(request_id)
    if not request:
        return {"message": "Request not found"}, 404

    # Find the next available nurse
    available_nurse = Nurse.query.filter_by(department=request.patient.room_number).first()
    if not available_nurse:
        return {"message": "No available nurse"}, 404

    # Assign the request to the nurse
    request.nurse_id = available_nurse.id
    request.save()
    return {"message": "Request escalated", "nurse_id": available_nurse.id}, 200