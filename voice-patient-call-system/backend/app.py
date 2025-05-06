# backend/app.py
from flask import Flask
from backend.config import Config_db
from backend.db import db

def create_app(config_class=Config_db):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)

    # Import and register routes
    from backend.routes.patient_routes import patient_bp
    from backend.routes.nurse_routes import nurse_bp

    app.register_blueprint(patient_bp, url_prefix='/api/patient')
    app.register_blueprint(nurse_bp, url_prefix='/api/nurse')

    return app