print("Ввод: ")
down = int(input("Введите нижнюю границу "))
up = int(input("Введите верхнюю границу "))
step = int(input("Введите шаг "))
print("C    F")
while up > down:
    F = down * 1.8 + 32
    print(f"{down}  {F}")
    down += step

down = up
F = up * 1.8 + 32
print(f"{down}  {F}")