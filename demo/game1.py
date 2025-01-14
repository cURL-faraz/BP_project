from rich.console import Console
from rich.theme import Theme
from rich.table import Table
import time

custom_theme = Theme({"success": "green", "error": "red"})
console = Console(theme=custom_theme)
wall_a = []
wall_o = []
for i in range(10):
    l = []
    for j in range(10):
        l.append("l")
    wall_a.append(l)
    wall_o.append(l)

def generate_table(wall_a, wall_o):
    s = ""
    for i in range(1, 18):
        ss = ""
        if i % 2 != 0:
            for n in range(9):
                if wall_a[i // 2][n] == "A":
                    if n!=8:
                        ss += "   [success]|[/success]"
                    else:
                        ss+="   "
                else:
                    if n!=8:
                        ss += "   [error]|[/error]"
                    else:
                        ss +="   "
        else:  # Even rows
            for n in range(9):
                if wall_o[(i - 1) // 2][n] == "A":
                    if n!=8:
                        ss += "[success]---[/success]*"
                    else:
                        ss += "[success]---[/success]"
                else:
                    if n!=8:
                        ss += "[error]---[/error]*"
                    else:
                        ss += "[error]---[/error]"
        s += ss + "\n"
    return s

console.print(generate_table(wall_a, wall_o))
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
import time

custom_theme = Theme({"success": "green", "error": "red"})
console = Console(theme=custom_theme)
wall_a = []
wall_o = []
for i in range(10):
    l = []
    for j in range(10):
        l.append("l")
    wall_a.append(l)
    wall_o.append(l)

def generate_table(wall_a, wall_o):
    s = ""
    for i in range(1, 18):  
        ss = ""
        if i % 2 != 0:  
            for n in range(9):
                if wall_a[i // 2][n] == "A":
                    if n!=8:
                        ss += "   [success]|[/success]"
                    else:
                        ss+="   "
                else:
                    if n!=8:
                        ss += "   [error]|[/error]"
                    else:
                        ss +="   "
        else:  # Even rows
            for n in range(9):
                if wall_o[(i - 1) // 2][n] == "A":
                    if n!=8:  
                        ss += "[success]---[/success]*"
                    else:
                        ss += "[success]---[/success]"
                else:
                    if n!=8:
                        ss += "[error]---[/error]*"
                    else:
                        ss += "[error]---[/error]"  
        s += ss + "\n"
    return s

console.print(generate_table(wall_a, wall_o))
