import re
import bcrypt
import json
from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({"success": "green", "error": "red"})
console = Console(theme=custom_theme)

FILE_NAME = "users.json"
LAST_USERS_FILE = "last_users.json"

def save_to_file(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file)

def load_from_file(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def hasher(password):
    SALT = bcrypt.gensalt(8)
    return bcrypt.hashpw(password.encode(), SALT).hex()

def check(email):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.match(pattern, email)

def handle_user(user_names):
    user = input("username: ")
    password = input("password: ")

    if user in user_names:
        console.print("User already exists. Please login.", style="error")

        while not bcrypt.checkpw(password.encode(), bytes.fromhex(user_names[user]["password"])):
            console.print("Username or password is incorrect.", style="error")
            password = input("password: ")

        console.print("Login successful.", style="success")

    else:
        email = input("email: ")
        while not check(email):
            console.print("Enter a valid email address.", style="error")
            email = input("email: ")

        user_names[user] = {
            "user": user,
            "password": hasher(password),
            "email": email
        }
        save_to_file(user_names, FILE_NAME)
        console.print("Registration successful.", style="success")
    
    return user

user_names = load_from_file(FILE_NAME)

console.print("Enter details for the first user:", style="success")
first_user = handle_user(user_names)

console.print("\nEnter details for the second user:", style="success")
second_user = handle_user(user_names)

last_users = {"first_user": first_user, "second_user": second_user}
save_to_file(last_users, LAST_USERS_FILE)

console.print("Current users data:", style="success")
print(user_names)

console.print("\nLast two users have been saved to 'last_users.json'", style="success")