from flask_marshmallow import Marshmallow
from marshmallow import fields, pre_load
from src.models import Patient
from src.utils import capitalize_names

# instance MA
ma = Marshmallow()

class PatientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Patient 
        load_instance = True
    
    #validate required fields
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)

    @pre_load
    def preprocess_data(self, data, **kwargs):
        return capitalize_names(data)
    
    phone = fields.String()
    email = fields.Email()
    address = fields.String()
    created_at = fields.DateTime(dump_only=True)
