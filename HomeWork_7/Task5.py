a = int(input("Введите значение A "))
b = int(input("Введите значение B "))
c = int(input("Введите значение С "))

for n in range(b,a-1,c):
    decision = n ** 3 + 2 * n**2 - 4 * n + 1
    print(f"В точке {n} функция равна {decision}")