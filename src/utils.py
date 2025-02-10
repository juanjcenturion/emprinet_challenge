import re

def capitalize_names(data):
    if 'first_name' in data:
        data['first_name'] = data['first_name'].capitalize()
    if 'last_name' in data:
        data['last_name'] = data['last_name'].capitalize()
    return data


def validate_email(email):
    # regular expression to validate email
    if email is not None:
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
        if re.match(patron, email):
            return True
        else:
            return False