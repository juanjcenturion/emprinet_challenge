import logging
from marshmallow import ValidationError

from src.models import Patient, Appointment, db
from src.schemas import PatientSchema
from src.configs.log_config import logger


# Service search by id 
def get_patient_by_id(id):
    logger.info(f"🔍 Buscando paciente con ID: {id} ")
    return Patient.query.filter_by(id=id, active=True).first()

# service query patients
def get_all_patients():
    logger.info(f"📋 Obteniendo pacientes activos")
    return Patient.query.filter_by(active=True).order_by(Patient.last_name)


# create new patient service
def create_patient(data):
    patient_schema = PatientSchema()

    # Validate and load data
    try:
        patient = patient_schema.load(data)
        db.session.add(patient)
        db.session.commit()

        logger.info(f"✅ Paciente creado correctamente: {patient.id} - {patient.last_name}, {patient.first_name}")

        return patient
    
    # Validation Error
    except ValidationError as err:
        logger.error(f"❌ Error al validar paciente: {err.messages}")
        return None, err.messages
    
    # Critical POST METHOD Error
    except Exception as e:
        logger.critical(f"🔥 Error crítico al crear paciente: {str(e)}")
        return None, {"error": "Error interno del servidor"}

# Service update patient
def update_patient(id, data):
    patient = Patient.query.filter_by(id=id, active=True).first()

    if not patient:
        logger.warning(f"⚠️ Paciente con ID {id} no encontrado para actualización.")
        return None, "Paciente no encontrado."

    patient_schema = PatientSchema()

    try:
        # Validate new data
        validated_data = patient_schema.load(data, partial=True)

    # Validation Error
    except ValidationError as err:
        logger.error(f"❌ Error en validación de actualización: {err.messages}")
        return None, err.messages
    
    # Critical PUT METHOD Error
    except Exception as e:
        logger.critical(f"🔥 Error crítico al editar el paciente: {str(e)}")
        return None, {"error": "Error interno del servidor"}

    # update data 
    for key, value in data.items():
        if hasattr(patient, key) and value is not None:
            setattr(patient, key, value)

    db.session.commit()
    logger.info(f"✅ Paciente con ID {id} actualizado correctamente.")
    return patient, None

# delete logic patient
def delete_patient(id):
    patient = Patient.query.filter_by(id=id, active=True).first()

    if not patient:
        logger.warning(f"⚠️ El paciente con ID {id}, no existe.")
        return None, "Paciente no encontrado"

    # Verify appointments
    assigned_appointments = Appointment.query.filter_by(patient_id=id).all()

    if assigned_appointments:
        logger.warning(f"⚠️ El paciente {id}, tiene turnos asignados, no se puede eliminar.")
        return None, "El paciente tiene turnos asignados, no se puede eliminar"

    patient.active = False
    db.session.commit()
    logger.info(f"🗑️ Paciente con ID {id} eliminado correctamente.")
    return patient, None
