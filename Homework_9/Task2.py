number = int(input("Введите длину лестницы -- > "))
for i in range(number+1):
    for n in range(i):
        print(i, end = "")
    if i != 0:
        print()

