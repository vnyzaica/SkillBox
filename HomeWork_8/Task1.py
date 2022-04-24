day_week = input("Введите день недели: ")
day_week = day_week.lower()
if day_week == "понедельник":
    print(1)
elif day_week == "вторник":
    print(2)
elif day_week == "среда":
    print(3)
elif day_week == "четверг":
    print(4)
elif day_week == "пятница":
    print(5)
elif day_week == "суббота":
    print(6)
elif day_week == "воскресенье":
    print(7)
else:
    print("Введите корректный день недели")