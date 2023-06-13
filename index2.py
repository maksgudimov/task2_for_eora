import csv

reask = 0
correct = 0
operator = 0

with open('table.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if float(row[1]) < 87 and float(row[1]) >= 38:
            reask+=1

        if float(row[1]) <= 100 and float(row[1]) >= 87:
            correct+=1

        if float(row[1]) < 38 and float(row[1]) >= 0:
            operator+=1

print(f"kolvo reask = {reask}")
print(f"kolvo correct = {correct}")
print(f"kolvo operator = {operator}")
