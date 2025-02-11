import sentry_sdk

from flask import Flask
from src.configs.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

# Sentry initialization
sentry_sdk.init(
    dsn="https://f72aae3ba40d6c34e435a9a4c61b7e24@o4507817865248768.ingest.us.sentry.io/4508800444203008",
    send_default_pii=True,
)

# Initialize app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize db, migrations, and JWT
db.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)

# Import views after app initialization to avoid circular imports
from src.views.patient_views import patient_blueprint
from src.views.appointement_views import appointment_blueprint
from src.views.user_views import user_blueprint

# Register blueprints
app.register_blueprint(patient_blueprint, url_prefix='/patients')
app.register_blueprint(appointment_blueprint, url_prefix='/appointments')
app.register_blueprint(user_blueprint, url_prefix='/auth')

# Main entry point for the app
if __name__ == "__main__":
    app.run(debug=True)
