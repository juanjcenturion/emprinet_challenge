from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flask.views import MethodView

from src.schemas import PatientSchema
from src.services.patient_service import (
    get_patient_by_id,
    get_all_patients,
    create_patient,
    update_patient, 
    delete_patient
)

class PatientsAPIView(MethodView):
    @jwt_required()
    def get(self, id=None):
        if id:
            # Search patient for id with service
            patient = get_patient_by_id(id)
            
            # Validate exists
            if not patient:
                return jsonify({"error": "Paciente no encontrado"}), 404
            
            patient_schema = PatientSchema()
            return patient_schema.jsonify(patient)
        
        # set default values for pagination
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 5, type=int)

        # Get query patients paginate
        patients_paginated = get_all_patients().paginate(
            page=page,
            per_page=per_page,error_out=False
        )

        # Serialize data
        patients_schema = PatientSchema(many=True)
        patients_data = patients_schema.dump(patients_paginated.items)

        # response whit pagination's metadata
        return jsonify({
            "patients": patients_data,
            "total": patients_paginated.total,
            "pages": patients_paginated.pages,
            "current_page": patients_paginated.page,
            "per_page": patients_paginated.per_page,
            "has_next": patients_paginated.has_next,
            "has_prev": patients_paginated.has_prev
        })
    
    @jwt_required()
    def post(self):
        data = request.get_json()

        # Create Patient whit service
        patient, errors = create_patient(data)

        if errors:
            return jsonify(errors), 400

        patient_schema = PatientSchema()
        return patient_schema.jsonify(patient), 201
    
    @jwt_required()
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

    @jwt_required()
    def delete(self, id):
        # delete patient
        patient, errors = delete_patient(id)

        if errors:
            return jsonify({"error": errors}), 400

        return jsonify({"message": "Paciente eliminado exitosamente."}), 200
    

