# API REST CHALLENGE BACKEND EMPRINET 4.0 🏥🐍

Este proyecto es una ***API REST*** desarrollada con __Flask__, __SQLAlchemy__ y __PostgreSQL__ para la gestión de pacientes y turnos medicos.

____
## 📌 Caracteristicas.
- __CRUD__ de pacientes y turnos médicos.
- Validación de datos con __Marshmallow__.
- Manejo de errores y respuestas JSON estructuradas.
- Conexión con __PostgreSQL__ mediante SQLAlchemy.
- Variables de entorno gestionadas con `.env`

## 🚀 Tecnologías Utilizadas.
- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Marshmallow
- Marshmallow
- PostgreSQL
- Dotenv
- Docker (opcional)

____

## 📦 Instalación y Configuración
add instalacion
____

## 📋 Endpoints Disponibles

#### Pacientes (`/parients`)
- `POST /patients` -> Crear pacientes.
- `GET /patients` -> Listar pacientes.
- `GET /patients/<id>` -> Obtener paciente por id.
- `PUT /patients/<id>` -> Actualizar/editar paciente.
- `DELETE /patients/<id>` -> Eliminación logica de paciente.

#### Turnos (`/appointments`)
- `POST /appointments` -> Crear turno.
- `GET /appointments` -> Listar turnos.
- `GET /appointments/<id>` -> Obtener turno por id.
- `PUT /appointments/<id>` -> Actualizar/editar turno.
- `DELETE /appointments/<id>` -> Eliminación logica de turno.

____
## 📂 Estructura del proyecto
```
📁emprinet_challenge/
|-- 📄 app.py    
|-- 📄 requirements.txt
|-- 📄 .env.example
|-- 📁 migrations
|-- 📁 src/
    |-- 📄 config.py
    |-- 📄 models.py
    |-- 📄 schemas.py
    |-- 📄 utils.py
    |-- 📁 configs/
        |-- 📄 config.py
        |-- 📄 log_config.py
    |-- 📁 logs/
    |-- 📁 services/
        |-- 📄 appointment_service.py
        |-- 📄 patient_service.py
        |-- 📄 user_service.py
    |-- 📁 utils/
        |-- 📄 utils.py
    |-- 📁 views/
        |-- 📄 appointment_views.py
        |-- 📄 patient_views.py
        |-- 📄 user_views.py
```

____

## 🔐 Extras Opcionales
1. Autenticación con JWT.
2. Paginación en listados.
3. Logging con Python Logging
4. Soporte para Docker.