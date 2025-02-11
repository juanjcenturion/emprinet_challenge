from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flask.views import MethodView

from src.schemas import AppointmentSchema

from src.services.appointment_service import (
    get_appointment_by_id,
    get_all_appointments,
    create_appointment,
    update_appointment,
    delete_appointment
)

class AppointmentsAPIView(MethodView):
    @jwt_required()
    def get(self, id=None):
        if id:
            # Search Appointments for id with service
            appointment = get_appointment_by_id(id)
            
            # Validate exists
            if not appointment:
                return jsonify({"error": "Turno no encontrado"}), 404
            
            appointment_schema = AppointmentSchema()
            return appointment_schema.jsonify(appointment)
        
        # Set default values for pagination
        page= request.args.get("page", 1, type=int)
        per_page= request.args.get("per_page", 5, type=int)
        
        # Get query appointments paginate
        appointments_paginated = get_all_appointments().paginate(
            page=page,
            per_page=per_page,error_out=False
        )

        #Serialize data
        appointment_schema = AppointmentSchema(many=True)
        appointments_data = appointment_schema.dump(appointments_paginated.items)
        
        # response whit pagination's metadata
        return jsonify({
            "appointments": appointments_data,
            "total": appointments_paginated.total,
            "pages": appointments_paginated.pages,
            "current_page": appointments_paginated.page,
            "per_page": appointments_paginated.per_page,
            "has_next": appointments_paginated.has_next,
            "has_prev": appointments_paginated.has_prev
        })
    
    @jwt_required()
    def post(self):
        data = request.get_json()
        
        appointment, errors = create_appointment(data)

        if errors:
            return jsonify(errors), 400
        
        appointment_schema = AppointmentSchema()
        return jsonify({
            "message": "Turno creado correctamente",
            "data": appointment_schema.dump(appointment) }),200

    @jwt_required()
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
    
    @jwt_required()
    def delete(self, id):
        # delete appointment
        appointment, errors = delete_appointment(id)

        if errors:
            return jsonify({"error": errors}), 400

        return jsonify({"message": "Turno eliminado exitosamente."}), 200