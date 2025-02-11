from datetime import timedelta

from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from src.models import User
from src.configs.log_config import logger


def register_user(username, password):
    # Verify if exists the username
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        logger.error(f"❌ El usuario {username} ya existe.")
        return {"error": "User already exists"}, 400

    # Generate hashed password
    hashed_password = generate_password_hash(password, method="pbkdf2", salt_length=16)

    # Create new User
    new_user = User(username=username, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    logger.info(f"✅ Nuevo usuario registrado: {username}")
    return {"message": "User registered successfully"}, 201


def login_user(username, password):
    user = User.query.filter_by(username=username).first()

    # Validate Username and password
    if not user or not check_password_hash(user.password_hash, password):
        logger.warning((f"⚠️ Credenciales incorrectas."))
        return {"error": "Invalid username or password"}, 401

    try:
        access_token = create_access_token(
            identity=username, expires_delta=timedelta(days=10)
        )
        logger.info(f"✅ Inicio de sessión exitoso, Usuario {username}")
        return {"message": "Login successful", "access_token": access_token}, 200
    except Exception as e:
        logger.critical(f"🔥 Error al generar el token: {str(e)}")
        return {"error": "Internal server error"}, 500
