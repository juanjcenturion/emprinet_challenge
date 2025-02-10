from flask_marshmallow import Marshmallow
from marshmallow import fields, pre_load, ValidationError
from src.models import Patient
from src.utils import capitalize_names, validate_email

# instance MA
ma = Marshmallow()

class PatientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Patient 
        load_instance = True
    
    #validate required fields
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email()

    @pre_load
    def preprocess_data(self, data, **kwargs):
        data = capitalize_names(data)
        if not validate_email(data.get("email", "")):
            raise ValidationError("Correo electrónico no válido.")
        return data
        
    
    
    phone = fields.String()
    address = fields.String()
    created_at = fields.DateTime(dump_only=True)
