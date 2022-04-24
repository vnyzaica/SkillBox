footer = int(input("Введите длину колонтитула: "))
importance = int(input("Введите важность сообщения: "))
time = (footer - importance) // 2
if (footer - importance) % 2 == 1:
    even = 1
else:
    even = 0
print("~"*time + "!" * importance + "~"*(time + even))