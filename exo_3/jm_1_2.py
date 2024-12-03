import os
import re

# Permet de récupérer le chemin d'accès du script
main_path = os.path.dirname(__file__)
# On crée le chemin d'accès vers notre fichier 
input = os.path.join(main_path, "input_jm.txt")
pattern = r"(mul\(\d+,\d+\)|don't\(\)|do\(\))"

with open(input, 'r') as f:
    data = f.read()
    cleaned_data = re.findall(pattern, data)

print(cleaned_data)

score = 0

valid = 0

for element in cleaned_data :
    if element == "do()" :
        valid = 0
    if element == "don't()" :
        valid = 1
    if valid == 0 and "mul" in element:
        element =  re.sub(r"[^\d,]", "", element)
        numbers = element.split(",")
        score = score + (int(numbers[0])*int(numbers[1]))

print(score)