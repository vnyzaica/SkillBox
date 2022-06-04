import math
a = float(input("Введите А "))
b = float(input("Введите В "))
c = float(input("Введите С "))
print(f"Решаем уравнение {a}*x^2 + {b}*x + {c} = 0")
d = (b ** 2 - 4 * a * c) ** (0.5)
if d < 0:
    print("Нет решений")
elif d == 0:
    x = b * -1 / (2 * a)
    print(x)
else:
    x1 = (b * -1 + d)/ (2 * a)
    x2 = (b * -1 - d)/ (2 * a)
    print(x1)
    print(x2)
