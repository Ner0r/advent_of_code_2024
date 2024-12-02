import os
import copy

# Permet de récupérer le chemin d'accès du script
main_path = os.path.dirname(__file__)
# On crée le chemin d'accès vers notre fichier 
input = os.path.join(main_path, "input_jm.txt")

first_list = []
safe_list = 0

def safelist (data) :
    if int(data[0]) < int(data[1]) : 
        for i in range (len(data)-1) :
            if int(data[i]) > int(data[i+1]) or abs(int(data[i]) - int(data[i+1])) > 3 or abs(int(data[i]) - int(data[i+1])) < 1  : 
                return 1
        return 0
    elif int(data[0]) > int(data[1]) : 
        for i in range (len(data)-1) :
            if int(data[i]) < int(data[i+1]) or abs(int(data[i]) - int(data[i+1])) > 3 or abs(int(data[i]) - int(data[i+1])) < 1  : 
                return 1
        return 0
            
            


with open(input, 'r') as f:
    for line in f : 
        data = line.split()
        if safelist(data) == 0 :
            safe_list += 1
        else : 
            for i in range(len(data)) :
                data2 = copy.deepcopy(data)
                data2.pop(i)
                if safelist(data2) == 0 :
                    safe_list += 1
                    break

print(safe_list)
        
        




