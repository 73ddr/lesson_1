distance = int(input("Дистанция в первый день:" ))
goal = int(input("Какая цель:" ))
days = 1
while distance < goal:
    distance *= 1.1
    days += 1
print(f"Необходимое число дней - {days} ")