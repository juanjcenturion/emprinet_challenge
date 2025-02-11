from flask import request, jsonify
from flask.views import MethodView
from marshmallow import ValidationError

from src.schemas import UserSchema
from src.services.user_service import register_user, login_user
from src.configs.log_config import logger


class RegisterAPIView(MethodView):
    def post(self):
        # get data from request
        data = request.get_json()

        # Validate data
        user_schema = UserSchema()
        try:
            # Validate and return dictionary
            valid_data = user_schema.load(data)
            logger.info(f"✅ Datos válidos para el usuario: {valid_data}")
        except ValidationError as err:
            # Return error if faliure validation
            logger.error(f"❌ Error de validación en los datos: {err.messages}")
            return jsonify({"error": "Invalid data", "details": err.messages}), 400

        username = valid_data.get("username")
        password = valid_data.get("password")

        # Llamamos al servicio para registrar el usuario
        response = register_user(username, password)

        # if service return error
        if "error" in response:
            logger.error(
                f"❌ Error al registrar el usuario {username}: {response['error']}"
            )
            return jsonify(response), 400

        return jsonify(response), 201


class LoginAPIView(MethodView):
    def post(self):
        # get data from request
        data = request.get_json()

        # Validate data
        user_schema = UserSchema()

        try:
            # Validate and return dictionary
            valid_data = user_schema.load(data)
            logger.info(f"✅ Datos válidos para el usuario: {valid_data}")
        except ValidationError as err:
            # Return error if faliure validation
            logger.error(f"❌ Error de validación en los datos: {err.messages}")
            return jsonify({"error": "Invalid data", "details": err.messages}), 400

        username = valid_data.get("username")
        password = valid_data.get("password")

        # Llamamos al servicio para el login
        response = login_user(username, password)

        # Si el servicio retorna un error, lo devolvemos
        if "error" in response:
            logger.error(
                f"❌ Error al intentar iniciar sesión para el usuario {username}: {response['error']}"
            )
            return jsonify(response), 401

        return jsonify(response), 200
