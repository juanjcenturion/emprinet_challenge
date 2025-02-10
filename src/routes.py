from flask import request, jsonify
from flask.views import MethodView
from marshmallow import ValidationError

from app import db
from src.models import Patient, Appointment
from src.schemas import PatientSchema

class PatientsRoute(MethodView):
    def get(self, id=None):
        if id:
            # search patient for id
            patient = Patient.query.filter_by(id=id, active=True).first()

            if not patient:
                return jsonify({"error": "Paciente no encontrado"}), 404
            
            patient_schema = PatientSchema()
            return patient_schema.jsonify(patient)

        # Get all patients
        patients = Patient.query.filter_by(active=True).all()
        patients_schema = PatientSchema(many=True)
        return patients_schema.jsonify(patients)

    def post(self):
        data = request.get_json()

        patient_schema = PatientSchema()

        # validate data
        try:
            patient = patient_schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        db.session.add(patient)
        db.session.commit()

        return patient_schema.jsonify(patient), 201
    
    def put(self, id):
        # Search patient for id
        patient = Patient.query.filter_by(id=id, active=True).first()

        # Verificar si el paciente existe
        if not patient:
            return jsonify({"error": "Paciente no encontrado"}), 404

        patient_schema = PatientSchema()

        try:
            # Load and validate data
            patient_json = request.get_json()
            validated_data = patient_schema.load(patient_json, partial=True) # Only for validation
        except ValidationError as err:
            return jsonify(err.messages), 400

        for key, value in patient_json.items():
            if hasattr(patient, key) and value is not None:
                setattr(patient, key, value)

        db.session.commit()

        return jsonify({
            "message": "Paciente actualizado exitosamente",
            "data": patient_schema.dump(patient)
        }), 200

    def delete(self, id):
        # Search patient for id
        patient = Patient.query.filter_by(id=id, active=True).first()


        # Validate if exists
        if not patient:
            return jsonify({"error": "Paciente no encontrado."}), 404
        
        # Verify if patient have a appointments asigned
        assigned_appointments = Appointment.query.filter_by(patient_id=id).all()

        if assigned_appointments:
            return jsonify({"error": "El paciente tiene turnos asignados, no se puede eliminar"})
        
        patient.active = False
        db.session.commit()

        return jsonify({"message": "Paciente eliminado exitosamente."}), 200