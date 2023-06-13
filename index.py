import csv

reask = 0
correct = 0
operator = 0

reask_d = []
correct_d = []
operator_d = []

with open('table.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[2] == "reask":
            reask += 1
            reask_d.append(float(row[1]))
        if row[2] == "correct":
            correct += 1
            correct_d.append(float(row[1]))
        if row[2] == "operator":
            operator += 1
            operator_d.append(float(row[1]))


print(f"max reask = {max(reask_d)} , min reask = {min(reask_d)}")
print(f"max correct_d = {max(correct_d)} , min correct_d = {min(correct_d)}")
print(f"max operator_d = {max(operator_d)} , min operator_d = {min(operator_d)}")

sred_reask = sum(reask_d) / reask
sred_correct = sum(correct_d) / correct
sred_operator = sum(operator_d) / operator

print(f"Среднее reask = {sred_reask}",f"Среднее correct = {sred_correct}",f"Среднее operator = {sred_operator}")

answer = float(input())

if answer < 87 and answer >= 38:
    print("Переспросить пользователя")

if answer <= 100 and answer >= 87:
    print("Вывести ответ пользователю")

if answer < 38 and answer >= 0:
    print("Перевести на оператора")