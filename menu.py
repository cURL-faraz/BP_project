import re
import bcrypt
import json
from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({"success": "green", "error": "red"})
console = Console(theme=custom_theme)

FILE_NAME = "users.json"