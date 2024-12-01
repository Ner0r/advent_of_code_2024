import os

# Permet de récupérer le chemin d'accès du script
main_path = os.path.dirname(__file__)
# On crée le chemin d'accès vers notre fichier 
input = os.path.join(main_path, "input_jm.txt")

list_one = []
list_two = []
distance = 0

with open(input, 'r') as f:
    for line in f : 
        d = line.split()
        list_one.append(int(d[0]))
        list_two.append(int(d[1]))
list_one.sort()
list_two.sort()


for i in range (len(list_one)) :
    distance = distance + abs(list_one[i]-list_two[i])

print(distance)
