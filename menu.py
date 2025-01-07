user_names = load_from_file()

user = input("username: ")

if user in user_names:
    console.print("user already exists. Please login.", style="error")
    user = input("enter your username: ")
    while user not in user_names:
        console.print("username not found.", style="error")
        user = input("enter your username: ")
    
    password = input("password: ")
    while not bcrypt.checkpw(password.encode(), bytes.fromhex(user_names[user]["password"])):
        console.print("Username or password is incorrect.", style="error")
        password = input("password: ")

    console.print("Login successful.", style="success")

else:
    password = input("password: ")
    user_names[user] = {"user": user, "password": hasher(password)}

    def check(email):
        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        return re.match(pattern, email)

    email = input("email: ")
    while not check(email):
        console.print("Enter a valid email address.", style="error")
        email = input("email: ")

    user_names[user]["email"] = email
    save_to_file(user_names)