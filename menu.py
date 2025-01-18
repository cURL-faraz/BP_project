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

    #Leaderboard

    best=dict()
for i in range(1,4):
    best[i]=[]
scores=[]
for key in dict1.keys():
    scores.append((key,dict1[key]["W"],dict1[key]["L"]))
    
scores=sorted(scores,key=lambda x:x[1],reverse=True)

ctc=1 
index=0
current_val=scores[0][1]
while ctc!=4 and index<len(dict1.keys()):
    if scores[index][1]!=current_val:
        ctc+=1
        current_val=scores[index][1]
    if ctc<4:
        best[ctc].append(scores[index][0])
        best[ctc].append(f"{scores[index][1]}W")
        best[ctc].append(f"{scores[index][2]}L")
    index+=1


for i in best.keys():
    print(i,end=" : ")
    for j in best[i]:
        print(j,end=" ")
    print()