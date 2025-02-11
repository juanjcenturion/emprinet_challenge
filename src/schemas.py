from datetime import datetime

from flask_marshmallow import Marshmallow
from marshmallow import fields, pre_load, post_dump, validate

from src.models import Patient, Appointment
from src.utils.utils import capitalize_names

# instance MA
ma = Marshmallow()


class UserSchema(ma.SQLAlchemyAutoSchema):
    username = fields.String(required=True, validate=validate.Length(min=3))
    password = fields.String(required=True, validate=validate.Length(min=6))


class PatientSchema(ma.SQLAlchemyAutoSchema):
    # validate required fields
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

    class Meta:
        model = Patient
        load_instance = True
        # Exclude fields unnecesary
        exclude = ("created_at", "updated_at", "active")

    @post_dump
    def remove_null_fields(self, data, **kwargs):
        # delete field null or none in response JSON
        return {key: value for key, value in data.items() if value is not None}


class AppointmentSchema(ma.SQLAlchemyAutoSchema):
    patient_id = fields.Integer(required=True)
    doctor = fields.String(required=True)
    specialty = fields.String(required=True)
    appointment_date = fields.DateTime(required=True, default=datetime.now)
    description = fields.String(required=False)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    active = fields.Boolean(default=True)

    patient = fields.Nested("PatientSchema", only=["id", "first_name", "last_name"])

    class Meta:
        model = Appointment
        include_relationships = True
        load_instance = True
        # Exclude fields unnecesary
        exclude = ("created_at", "updated_at", "active")

    @post_dump
    def remove_null_fields(self, data, **kwargs):
        # delete field null or none in response JSON
        return {key: value for key, value in data.items() if value is not None}
