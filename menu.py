import re
import bcrypt
import json
from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({"success": "green", "error": "red"})
console = Console(theme=custom_theme)

FILE_NAME = "users.json"

def save_to_file(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file)

def load_from_file():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def hasher(password):
    SALT = bcrypt.gensalt(8)
    hexpass = bcrypt.hashpw(password.encode(), SALT).hex()
    return hexpass     