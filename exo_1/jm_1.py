import os
import copy
import sys


# Afficher la limite d'occurence du système
print(sys.getrecursionlimit())

# Changer le nombre d'occurence max à 10k
sys.setrecursionlimit(10000)

# Permet de récupérer le chemin d'accès du script
main_path = os.path.dirname(__file__)
# On crée le chemin d'accès vers notre fichier 
input = os.path.join(main_path, "input_jm.txt")

def path (data, electric_data, position, direction , list_of_position) :
    # for element in electric_data :
    #     print(element)
    # print(direction)
    # print(position)
    # print()
    try :
        x = position[0]
        y = position[1]
        if not (x < 0 or y < 0) :
            list_of_position.append((x,y,direction))
            # Si le caractère est un point :
            if data[y][x] == "." :
                electric_data[y][x] = "#"
                if direction == "G" :
                    x += 1
                elif direction == "D" :
                    x -= 1
                elif direction == "H" :
                    y += 1
                elif direction == "B" :
                    y -= 1
                if not (x,y,direction) in list_of_position :
                    path(data, electric_data,(x,y), direction , list_of_position)
            
            # Si le caractère est un - :
            elif data[y][x] == "-" :
                electric_data[y][x] = "#"
                if direction == "G" :
                    x += 1
                    if not (x,y,direction) in list_of_position :
                        path(data, electric_data,(x,y), direction, list_of_position)
                elif direction == "D" :
                    x -= 1
                    if not (x,y,direction) in list_of_position :
                        path(data, electric_data,(x,y), direction, list_of_position)
                elif direction == "H" or direction == "B" :
                    x_1 = x + 1
                    x_2 = x - 1
                    if not (x_1,y,"G") in list_of_position :
                        path(data, electric_data,(x_1,y), "G", list_of_position)
                    if not (x_2,y,"D") in list_of_position :
                        path(data, electric_data,(x_2,y), "D", list_of_position)

            
            # Si le caractère est un | :

            elif data[y][x] == "|" :

                electric_data[y][x] = "#"
                if direction == "G" or direction == "D":
                    y_1 = y + 1
                    y_2 = y - 1
                    if not (x,y_1,"H") in list_of_position :
                        path(data, electric_data,(x,y_1), "H", list_of_position)
                    if not (x,y_2,"B") in list_of_position :
                        path(data, electric_data,(x,y_2), "B", list_of_position)

                elif direction == "H" :
                    y += 1
                    if not (x,y,direction) in list_of_position :
                        path(data, electric_data,(x,y), direction, list_of_position)
                elif direction == "B" :
                    y -= 1
                    if not (x,y,direction) in list_of_position :
                        path(data, electric_data,(x,y), direction, list_of_position)
            
            # Si le caractère est un / :

            elif data[y][x] == "/" :
                electric_data[y][x] = "#"
                if direction == "G" :
                    y -= 1
                    if not (x,y,"B") in list_of_position :
                        path(data, electric_data,(x,y), "B", list_of_position)

                elif direction == "D" :
                    y += 1
                    if not (x,y,"H") in list_of_position :
                        path(data, electric_data,(x,y), "H", list_of_position)

                elif direction == "H" :
                    x -= 1
                    if not (x,y,"D") in list_of_position :
                        path(data, electric_data,(x,y), "D", list_of_position)

                elif direction == "B" :
                    x += 1
                    if not (x,y,"G") in list_of_position :
                        path(data, electric_data,(x,y), "G", list_of_position)
            
            # Si le caractère est un \ :

            elif data[y][x] == "\\" :
            
                electric_data[y][x] = "#"

                if direction == "G" :
                    y += 1
                    if not (x,y,"H") in list_of_position :
                        path(data, electric_data,(x,y), "H", list_of_position)
                elif direction == "D" :
                    y -= 1
                    if not (x,y,"B") in list_of_position :
                        path(data, electric_data,(x,y), "B", list_of_position)
                elif direction == "H" :
                    x += 1
                    if not (x,y,"G") in list_of_position :
                        path(data, electric_data,(x,y), "G", list_of_position)
                elif direction == "B" :
                    x -= 1
                    if not (x,y,"D") in list_of_position :
                        path(data, electric_data,(x,y), "D", list_of_position)
    
    # On peut préciser l'erreur qu'on except (si on veut un type d'erreur spécifique). OverflowError, IndexError > index out of range
    except IndexError:
        return None

data = []

with open(input, 'r') as f:
    for line in f : 
        data.append(list(line.rstrip("\n")))

list_of_position = []
electric_path = copy.deepcopy(data)

# Haut
#start = (3,0)
#path(data,electric_path, start, "H", list_of_position)

# Bas
#start = (3,4)
#path(data,electric_path, start, "B", list_of_position)

# Gauche => droite
#start = (0,2)
#path(data,electric_path, start, "G", list_of_position)

# Droite
#start = (9,2)
#path(data,electric_path, start, "D", list_of_position)

#position, direction , list_of_position)
start = (0,0)
path(data,electric_path, start, "G", list_of_position)
result = 0
#print(list_of_position)

#print(electric_path)
for element in electric_path :
    for item in element :
        if item == "#" :
            result += 1

print(result)

#6758

#7927