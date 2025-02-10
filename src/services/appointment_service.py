from src.models import Patient, Appointment, db
from marshmallow import ValidationError
from src.schemas import PatientSchema, AppointmentSchema

def get_appointment_by_id(id):
    # Method search appointment by id 
    return Appointment.query.filter_by(id=id, active=True).first()

def get_all_appointments():
    # Method list appointments
    return Appointment.query.filter_by(active=True).all()

# create new appointment service
def create_appointment(data):

    try:
        appointment_schema = AppointmentSchema()
        appointment = appointment_schema.load(data)
        db.session.add(appointment)
        db.session.commit()
        return appointment, None
    
    except ValidationError as err:
        return None, err.messages
    except Exception as e:
        return None, str(e)


# Update appointment service:
def update_appointment(id, data):
    appointment= Appointment.query.filter_by(id=id, active=True).first()

    if not appointment:
        return None, "Turno no encontrado."
    
    if not data:
        return None, "No hay datos para actualizar"
    
    appointment_schema = AppointmentSchema()

    try:
        # Validate new data
        validated_data = appointment_schema.load(data, partial=True)
    except ValidationError as err:
        return None, err.messages
    
    # Update data
    for key, value in data.items():
        if hasattr(appointment, key) and value is not None:
            setattr(appointment, key, value)
    
    db.session.commit()
    return appointment, None

# Logic delete service
def delete_appointment(id):
    appointment = Appointment.query.filter_by(id=id, active=True).first()

    if not appointment:
        return None, "Paciente no encontrado"

    appointment.active = False
    db.session.commit()

    return appointment, None