import re
import bcrypt
import json
from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({"success": "green", "error": "red"})
console = Console(theme=custom_theme)

FILE_NAME = "users.json"

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

def sign_up(user_names):
    user = input("Username: ")
    if user in user_names:
        console.print("User already exists. Please choose login.", style="error")
        return None

    password = input("Password: ")
    email = input("Email: ")
    while not check(email):
        console.print("Enter a valid email address.", style="error")
        email = input("Email: ")

    user_names[user] = {
        "password": hasher(password),
        "email": email
    }
    save_to_file(user_names, FILE_NAME)
    console.print("Registration successful.", style="success")
    return user

def login(user_names):
    user = input("Username: ")
    if user not in user_names:
        console.print("User not found. Please sign up.", style="error")
        return None

    password = input("Password: ")
    while not bcrypt.checkpw(password.encode(), bytes.fromhex(user_names[user]["password"])):
        console.print("Username or password is incorrect.", style="error")
        password = input("Password: ")

    console.print("Login successful.", style="success")
    return user

def get_second_user_credentials(user_names, first_user):
    console.print("\nEnter new player's credentials:", style="success")
    while True:
        user = input("Username: ")
        if user == first_user:
            console.print("Error: Second user cannot be the same as the first user.", style="error")
            continue

        if user in user_names:
            console.print(f"User {user} exists. Please enter the password to log in.", style="success")
            while True:
                password = input("Password: ")
                if bcrypt.checkpw(password.encode(), bytes.fromhex(user_names[user]["password"])):
                    console.print(f"User {user} logged in successfully. Starting new game...", style="success")
                    return user
                else:
                    console.print("Incorrect password. Please try again.", style="error")

        password = input("Password: ")
        email = input("Email: ")
        while not check(email):
            console.print("Enter a valid email address.", style="error")
            email = input("Email: ")

        user_names[user] = {
            "password": hasher(password),
            "email": email
        }
        save_to_file(user_names, FILE_NAME)
        console.print(f"User {user} registered successfully as the second player.", style="success")
        return user

def main_menu(user_names, first_user):
    console.print("\n1. Leaderboard\n2. Start New Game\n3. Logout\n4. Game History", style="success")
    choice = input("Choose an option: ")

    if choice == '1':
        console.print("Leaderboard feature coming soon!", style="success")
        return
    elif choice == '2':
        second_user = get_second_user_credentials(user_names, first_user)
        if second_user:
            console.print(f"Second user {second_user} logged in. Starting new game...", style="success")
        return
    elif choice == '3':
        console.print("Logging out...", style="success")
        exit(0)
    elif choice == '4':
        console.print("Game history feature coming soon!", style="success")
        return
    else:
        console.print("Invalid choice. Please restart the program.", style="error")
        return

def main():
    user_names = load_from_file(FILE_NAME)

    console.print("\n1. Login\n2. Sign Up", style="success")
    choice = input("Choose an option: ")
    user = None

    if choice == '1':
        user = login(user_names)
    elif choice == '2':
        user = sign_up(user_names)
    else:
        console.print("Invalid choice. Please restart the program.", style="error")
        return

    if user:
        main_menu(user_names, user)

if __name__ == "__main__":
    main()