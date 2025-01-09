import re
from rich.console import Console
from rich.theme import Theme
custom_theme =Theme({"success":"green","error":"red"})
console=Console(theme=custom_theme)
user_names ={}
user = input()

if user in user_names.keys():
    console.print("user already exists. Please login.",style="error")
else:
    password = input()
    user_names[user] = dict()
    user_names[user]["user"] = user
    user_names[user]["password"] = password
def check(a):
    pattern =r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    x = re.findall(pattern , a)
    return(x)
email = input()
while (check(email)) == []:
    console.print("Enter a valid email address.",style="error")
    # clear()
    email = input()
else:
    user_names[user]["email"] = email

    
console.print(user_names,style="success")