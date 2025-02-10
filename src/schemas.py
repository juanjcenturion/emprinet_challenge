from datetime import datetime

from flask_marshmallow import Marshmallow
from marshmallow import fields, pre_load, ValidationError

from src.models import Patient, Appointment
from src.utils import capitalize_names

# instance MA
ma = Marshmallow()

class PatientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Patient 
        load_instance = True
    
    #validate required fields
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email()

    @pre_load
    def preprocess_data(self, data, **kwargs):
        data = capitalize_names(data)
        return data
    
    phone = fields.String()
    address = fields.String()
    created_at = fields.DateTime(dump_only=True)



class AppointmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Appointment
        include_relationships = True
        load_instance = True

    patient_id = fields.Integer(required=True)
    doctor = fields.String(required=True)
    specialty = fields.String(required=True)
    appointment_date = fields.DateTime(required=True, default=datetime.now)
    notes = fields.String(required=False)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    active = fields.Boolean(default=True)

    patient = fields.Nested('PatientSchema', only=['id', 'first_name', 'last_name'])

    def __str__(self):
        return f"Appointment for Patient ID: {self.patient}, Doctor: {self.doctor}, Date: {self.appointment_date}"
