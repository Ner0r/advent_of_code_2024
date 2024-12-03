import os
import re

# Permet de récupérer le chemin d'accès du script
main_path = os.path.dirname(__file__)
# On crée le chemin d'accès vers notre fichier 
input = os.path.join(main_path, "input_jm.txt")

with open(input, 'r') as f:
    data = f.read()
    cleaned_data = re.findall(r"mul\(\d+,\d+\)", data)

score = 0

for element in cleaned_data :
    element =  re.sub(r"[^\d,]", "", element)
    numbers = element.split(",")
    score = score + (int(numbers[0])*int(numbers[1]))

print(score)


