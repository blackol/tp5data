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