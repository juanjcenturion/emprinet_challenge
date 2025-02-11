from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.configs.config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

# Instance the App
app = Flask(__name__)
app.config.from_object(Config)

# init db and migrations 
db.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)

# Api route imports before init db and migrate to avoid generating circular import
from src.views.patient_views import PatientsAPIView
from src.views.appointement_views import AppointmentsAPIView
from src.views.user_views import RegisterAPIView, LoginAPIView

# Add routes to app
app.add_url_rule("/register", view_func=RegisterAPIView.as_view('register'), methods=["POST"])
app.add_url_rule("/login", view_func=LoginAPIView.as_view('login'), methods=["POST"])
app.add_url_rule("/patients", view_func=PatientsAPIView.as_view('patients'), methods=["GET", "POST"])
app.add_url_rule("/patients/<int:id>", view_func=PatientsAPIView.as_view('patient'), methods=["GET", "PUT", "DELETE"])
app.add_url_rule("/appointments", view_func=AppointmentsAPIView.as_view('appointments'), methods=["GET", "POST"])
app.add_url_rule("/appointments/<int:id>", view_func=AppointmentsAPIView.as_view('appointment'), methods=["GET", "PUT", "DELETE"])

