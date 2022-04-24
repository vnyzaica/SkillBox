sum = 0
for i in range(10):
    cow = input("Введите наличие коров: ")
    if cow == "b":
        sum += (i+1) * 2

print(f"Всего {sum} литров.")