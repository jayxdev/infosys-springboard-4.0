from backend.db import db  # Use absolute import

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False, default='No content provided')
    category = db.Column(db.String(20), nullable=False)  # Routine, Urgent, Emergency
    status = db.Column(db.String(20), default='Pending')  # Pending, Completed
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    nurse_id = db.Column(db.Integer, db.ForeignKey('nurse.id'), nullable=True)

    def save(self):
        db.session.add(self)
        db.session.commit()