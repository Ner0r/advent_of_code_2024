import os

# Permet de récupérer le chemin d'accès du script
main_path = os.path.dirname(__file__)
# On crée le chemin d'accès vers notre fichier 
input = os.path.join(main_path, "input_jm.txt")

first_list = []
safe_list = 0


with open(input, 'r') as f:
    for line in f : 
        dangerous = 0
        data = line.split()

        if int(data[0]) < int(data[1]) : 
            for i in range (len(data)-1) :
                if int(data[i]) > int(data[i+1]) or abs(int(data[i]) - int(data[i+1])) > 3 or abs(int(data[i]) - int(data[i+1])) < 1  : 
                    dangerous = 1
            if dangerous == 0 :
                safe_list += 1

        elif int(data[0]) > int(data[1]) : 
            for i in range (len(data)-1) :
                if int(data[i]) < int(data[i+1]) or abs(int(data[i]) - int(data[i+1])) > 3 or abs(int(data[i]) - int(data[i+1])) < 1  : 
                    dangerous = 1
            if dangerous == 0 :
                safe_list += 1

        
print(safe_list)           




