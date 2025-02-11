import re


def capitalize_names(data):
    if "first_name" in data:
        data["first_name"] = data["first_name"].capitalize()
    if "last_name" in data:
        data["last_name"] = data["last_name"].capitalize()
    return data
