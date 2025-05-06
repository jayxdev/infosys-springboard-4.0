from backend.db import db  # Use absolute import

class Nurse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    department = db.Column(db.String(80), nullable=False)
    requests = db.relationship('Request', backref='nurse', lazy=True)

    def save(self):
        db.session.add(self)
        db.session.commit()