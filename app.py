from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.config import Config

db = SQLAlchemy()
migrate = Migrate()

# Instance the App
app = Flask(__name__)
app.config.from_object(Config)

# init db and migrations 
db.init_app(app)
migrate.init_app(app, db)

# Api route imports before init db and migrate to avoid generating circular import
from src.views.views import PatientsAPIView, AppointmentsAPIView

# Add routes to app
app.add_url_rule("/patients", view_func=PatientsAPIView.as_view('patients'), methods=["GET", "POST"])
app.add_url_rule("/patients/<int:id>", view_func=PatientsAPIView.as_view('patient'), methods=["GET", "PUT", "DELETE"])
app.add_url_rule("/appointments", view_func=AppointmentsAPIView.as_view('appointments'), methods=["GET", "POST"])
app.add_url_rule("/appointments/<int:id>", view_func=AppointmentsAPIView.as_view('appointment'), methods=["GET", "PUT", "DELETE"])

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
