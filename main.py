import csv 

# variable qui contient le nom du fichier csv
file_name = "Absenteeism_at_work.csv"

#fonction qui convertit un csv en dictionnaire de données et qui renvoie le dictionnaire de données sans module numpy
def csv_to_dict(file_name):
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = []
        for row in csv_reader:
            data.append(row)
    return data

#fonction qui convertit un csv en tableau de données et qui renvoie le tableau de données sans module numpy
def csv_to_array(file_name):
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        data = []
        for row in csv_reader:
            data.append(row)
    return data

#Afficher le contenu d'un tableau de données
def print_array(data):
    for row in data:
        print(row)


#fonction qui affiche le contenu d'un dictionnaire de données
def print_dict(data):
    for row in data:
        print(row)



#split (transforme une chaine de caractère en tableau)


#Programme principale ----------------------------------------------------------------------------------------------------

data = csv_to_array(file_name)
print(data)
print(1)
#data2 = get_column(data, 1)
#print(data2)

#----------------------------------------------------------------------------------------------------------------------
