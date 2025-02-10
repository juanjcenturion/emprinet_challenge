from flask import request, jsonify
from flask.views import MethodView

from src.schemas import PatientSchema, AppointmentSchema
from src.services.patient_service import (
    get_patient_by_id,
    get_all_patients,
    create_patient,
    update_patient, 
    delete_patient
)
from src.services.appointment_service import (
    get_appointment_by_id,
    get_all_appointments,
    create_appointment,
    update_appointment,
    delete_appointment
)

class PatientsAPIView(MethodView):
    def get(self, id=None):
        if id:
            # Search patient for id with service
            patient = get_patient_by_id(id)
            
            # Validate exists
            if not patient:
                return jsonify({"error": "Paciente no encontrado"}), 404
            
            patient_schema = PatientSchema()
            return patient_schema.jsonify(patient)
        
        # Get all patients with service
        patients = get_all_patients()
        patients_schema = PatientSchema(many=True)
        return patients_schema.jsonify(patients)

    def post(self):
        data = request.get_json()

        # Create Patient whit service
        patient, errors = create_patient(data)

        if errors:
            return jsonify(errors), 400

        patient_schema = PatientSchema()
        return patient_schema.jsonify(patient), 201
    
    def put(self, id):
        # Update patient whit service
        patient_json = request.get_json()
        patient, errors = update_patient(id, patient_json)

        if errors:
            return jsonify({"error": errors}), 404

        patient_schema = PatientSchema()
        return jsonify({
            "message": "Paciente actualizado exitosamente",
            "data": patient_schema.dump(patient)
        }), 200

    def delete(self, id):
        # delete patient
        patient, errors = delete_patient(id)

        if errors:
            return jsonify({"error": errors}), 400

        return jsonify({"message": "Paciente eliminado exitosamente."}), 200
    


class AppointmentsAPIView(MethodView):
    def get(self, id=None):
        if id:
            # Search Appointments for id with service
            appointment = get_appointment_by_id(id)
            
            # Validate exists
            if not appointment:
                return jsonify({"error": "Turno no encontrado"}), 404
            
            appointment_schema = AppointmentSchema()
            return appointment_schema.jsonify(appointment)
        
        #Get all Appointments with service
        appointments = get_all_appointments()
        appointment_schema = AppointmentSchema(many=True)
        return appointment_schema.jsonify(appointments)
    
    def post(self):
        data = request.get_json()
        
        appointment, errors = create_appointment(data)

        if errors:
            return jsonify(errors), 400
        
        appointment_schema = AppointmentSchema()
        return jsonify({
            "message": "Turno creado correctamente",
            "data": appointment_schema.dump(appointment) }),200

    def put(self, id):
        # Update appointment with service
        appointment_json = request.get_json()
        appointment, errors = update_appointment(id, appointment_json)

        if errors:
            return jsonify({"error": errors}), 400
        
        appointment_schema = AppointmentSchema()

        return jsonify({
            "message": "Turno actualizado exitosamente",
            "data": appointment_schema.dump(appointment)
        }), 200
    
    def delete(self, id):
        # delete appointment
        appointment, errors = delete_appointment(id)

        if errors:
            return jsonify({"error": errors}), 400

        return jsonify({"message": "Turno eliminado exitosamente."}), 200