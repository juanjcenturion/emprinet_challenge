from datetime import datetime

from app import db

class Patient(db.Model):
    
    __tablename__ = 'patient'

    # Table fields
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Appointment(db.Model):

    __tablename__= 'appointment'

    # Table fields
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    doctor = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    # Relationship
    patient = db.relationship('Patient', backref='appointment')

    def __str__(self):
        return f"{self.patient_id},  {self.appointment_date}>"
    