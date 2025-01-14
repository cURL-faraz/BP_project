from rich.console import Console
from rich.theme import Theme
custom_theme = Theme({})
console = Console(theme=custom_theme)
wall_a = []
wall_o = []
for i in range(9):
    l = []
    for j in range(9):
        l.append("Available")
    wall_a.append(l.copy())
    wall_o.append(l.copy())
red_position=[1,5]
blue_position=[9,5]
def block_wall_a(wall_a : list,x_center,y_center):
    if x_center <= 9 and y_center <= 9 :
        wall_a[x_center-1][y_center-1]="Blocked";wall_a[x_center][y_center-1]="Blocked"
        return(wall_a)
def block_wall_o(wall_o : list,x_center,y_center):
    if x_center <= 9 and y_center <= 9 :
        wall_o[x_center-1][y_center-1]="Blocked";wall_o[x_center-1][y_center]="Blocked"
        return(wall_o)

def generate_table(wall_a, wall_o,red_position,blue_position):
    s = ""
    for i in range(1, 18):  
        ss = ""
        if i % 2 != 0: 
            for n in range(9):
                if ((i+1)/2)==red_position[0] and n+1==red_position[1]:
                    if wall_a[(i-1) // 2][n] == "Available":
                        if n!=8:
                            ss += " [red]O[/red] [yellow2]|[/yellow2]"
                        else:
                            ss+=" [red]O[/red] "
                    else:
                        if n!=8:
                            ss += " [red]O[/red] [orange3]|[/orange3]"
                        else:
                            ss +=" [red]O[/red] "
                elif ((i+1)/2)==blue_position[0] and n+1==blue_position[1]:
                    if wall_a[(i-1) // 2][n] == "Available":
                        if n!=8:
                            ss += " [blue]O[/blue] [yellow2]|[/yellow2]"
                        else:
                            ss+=" [blue]O[/blue] "
                    else:
                        if n!=8:
                            ss += " [blue]O[/blue] [orange3]|[/orange3]"
                        else:
                            ss +=" [blue]O[/blue] "
                else:
                    if wall_a[(i-1) // 2][n] == "Available":
                        if n!=8:
                            ss += "   [yellow2]|[/yellow2]"
                        else:
                            ss+="   "
                    else:
                        if n!=8:
                            ss += "   [orange3]|[/orange3]"
                        else:
                            ss +="   "
        else: 
            for n in range(9):
                if wall_o[(i - 1) // 2][n] == "Available":
                    if n!=8:  
                        ss += "[yellow2]——-[/yellow2]o"
                    else:
                        ss += "[yellow2]——-[/yellow2]"
                else:
                    if n!=8:
                        ss += "[orange3]——-[/orange3]o"
                    else:
                        ss += "[orange3]——-[/orange3]"  
        s += ss + "\n"
    return s
console.print(generate_table(wall_a, wall_o,red_position,blue_position))

