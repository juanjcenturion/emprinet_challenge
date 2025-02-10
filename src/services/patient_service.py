from marshmallow import ValidationError

from src.models import Patient, Appointment, db
from src.schemas import PatientSchema


# Service search by id 
def get_patient_by_id(id):
    return Patient.query.filter_by(id=id, active=True).first()

# service query patients
def get_all_patients():
    return Patient.query.filter_by(active=True).order_by(Patient.last_name)


# create new patient service
def create_patient(data):
    patient_schema = PatientSchema()

    # Validate and load data
    try:
        patient = patient_schema.load(data)
        db.session.add(patient)
        db.session.commit()
        return patient
    except ValidationError as err:
        return None, err.messages

# Service update patient
def update_patient(id, data):
    patient = Patient.query.filter_by(id=id, active=True).first()

    if not patient:
        return None, "Paciente no encontrado."

    patient_schema = PatientSchema()

    try:
        # Validate new data
        validated_data = patient_schema.load(data, partial=True)
    except ValidationError as err:
        return None, err.messages

    # update data 
    for key, value in data.items():
        if hasattr(patient, key) and value is not None:
            setattr(patient, key, value)

    db.session.commit()
    return patient, None

# delete logic patient
def delete_patient(id):
    patient = Patient.query.filter_by(id=id, active=True).first()

    if not patient:
        return None, "Paciente no encontrado"

    # Verify appointments
    assigned_appointments = Appointment.query.filter_by(patient_id=id).all()

    if assigned_appointments:
        return None, "El paciente tiene turnos asignados, no se puede eliminar"

    patient.active = False
    db.session.commit()
    return patient, None
