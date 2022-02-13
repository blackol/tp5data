import csv

file = csv.reader(open('Absenteeism_at_work.csv', 'r'))

title = next(file)    
datas = []

for row in file:
    for i in range(len(row)):
        temp = row[i].split(";")
        temp = [float(i) for i in temp]
        datas.append(temp)

print(datas[2][3])

#discretize
infos = {}

for i in datas:
    for j in i:
        if j not in infos:
            infos[j] = 1
        else:
            infos[j] += 1

for i in infos:
    print(i, infos[i], sep = ": ", end = "\n")