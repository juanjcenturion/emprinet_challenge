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

#### 1. Clonar el repositorio
```
git clone https://github.com/juanjcenturion/emprinet_challenge.git
cd emprinet_challenge
```
#### 2. Crear y activar tu entorno virtual (opcional)
```
python3 -m venv venv
source venv/bin/activate  # En Linux/macOS
venv\Scripts\activate  # En Windows
```
#### 3. Instalar Dependecias
```
pip install -r requirements.txt
```
#### 4. Configurar variables de entorno
```
cp .env.example .env
```
edita el archivo .env correctamente con tus credenciales

#### 5. Inicializar la base de datos
```
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```
#### 6. Ejecutar el proyecto:
```
flask run --reload
```
____
## 🐳 Despliegue de la Aplicación con Docker-Compose
Si prefieres usar Docker para ejecutar la aplicación, sigue estos pasos:
#### 1️. Construir y ejecutar los contenedores

`docker-compose up --build -d`
- `build`: recontruye las imagenes en cambio de codigo
- `-d`: ejecuta los contenedores en segundo plano (opcional)

#### 2. Verificar que los contenedores están corriendo
```docker ps```
- Deberías ver los contenedores de la app flask y postresql, corriendo

#### 3. Ver los logs de la aplicación (opcional)
- Si necesitas revisar los registros de Flask, usa:
`docker logs -f emprinet_flask_app`
- Si necesitas revisar PostgreSQL:
`docker logs -f postgres_database`
____

## 📋 Endpoints Disponibles

#### Pacientes (`/patients`)
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

#### Autenticación (`/auth`)
- `POST /auth/register` -> Crear Usuario.
- `POST /auth/login` -> Iniciar sesión.

____
## 📂 Estructura del proyecto
```
📁emprinet_challenge/
|-- 📄 app.py    
|-- 📄 requirements.txt
|-- 📄 .env.example
|-- 📄 Dockerfile
|-- 📄 docker-compose.yml
|-- 📄 run.sh
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
    |-- 📁 tests/
        |-- 📄 auth_test.py
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
3. Logging con Python Logging.
4. Soporte para Docker.
5. Sentry