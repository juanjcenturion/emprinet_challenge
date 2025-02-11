from src.models import Patient, Appointment, db
from marshmallow import ValidationError

from src.schemas import AppointmentSchema
from src.configs.log_config import logger


def get_appointment_by_id(id):
    # Method search appointment by id
    logger.info(f"🔍 Buscando turno con ID: {id} ")
    return Appointment.query.filter_by(id=id, active=True).first()

def get_all_appointments():
    # Method list appointments
    logger.info("📋 Obteniendo turnos activos")
    return Appointment.query.filter_by(active=True).order_by(Appointment.appointment_date)

# create new appointment service
def create_appointment(data):

    try:
        appointment_schema = AppointmentSchema()
        appointment = appointment_schema.load(data)
        db.session.add(appointment)
        db.session.commit()

        logger.info(f"✅ Turno creado correctamente: {appointment.id}")

        return appointment, None
    
    except ValidationError as err:
        logger.error(f"❌ Error al validar el turno: {err.messages}")
        return None, err.messages
    except Exception as e:
        logger.critical(f"🔥 Error crítico al crear el turno: {str(e)}")
        return None, {"error": "Error interno del servidor"}


# Update appointment service:
def update_appointment(id, data):
    appointment= Appointment.query.filter_by(id=id, active=True).first()

    if not appointment:
        logger.warning(f"⚠️ Turno con ID {id} no encontrado")
        return None, "Turno no encontrado."
    
    if not data:
        logger.warning(f"⚠️ No hay datos para actualizar")
        return None, "No hay datos para actualizar"
    
    appointment_schema = AppointmentSchema()

    try:
        # Validate new data
        validated_data = appointment_schema.load(data, partial=True)
    
    #Validation error
    except ValidationError as err:
        logger.error(f"❌ Error en validación de actualización: {err.messages}")
        return None, err.messages
    
    #Critical PUT METHOD Error
    except Exception as e:
        logger.critical(f"🔥 Error crítico al editar el turno: {str(e)}")
        return None, {"error": "Error interno del servidor"}
    
    # Update data
    for key, value in data.items():
        if hasattr(appointment, key) and value is not None:
            setattr(appointment, key, value)
    
    db.session.commit()
    logger.info(f"✅ Turno con ID {id} actualizado correctamente.")
    return appointment, None

# Logic delete service
def delete_appointment(id):
    appointment = Appointment.query.filter_by(id=id, active=True).first()

    if not appointment:
        logger.warning(f"⚠️ El Turno con ID {id}, no existe.")
        return None, "Turno no encontrado"

    appointment.active = False
    db.session.commit()
    logger.info(f"🗑️ El turno con ID {id} eliminado correctamente.")

    return appointment, None