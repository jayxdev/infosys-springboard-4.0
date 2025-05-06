import unittest
from backend import app, db
from models.patient import Patient

class TestAuth(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_patient_signup(self):
        response = self.app.post('/api/patient/signup', json={
            "username": "test_patient",
            "password": "test123",
            "room_number": "101"
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()