import math
numbers = int(input("Введите количество чисел: "))
for i in range(numbers):
    num = float(input("Введите число "))
    num = int(num)
    if num < 0:
        num -= 1
        print(f"x = {num}  ",end = "")
        num = math.exp(num)
        print(f"exp(x) = {num}")
    elif num > 0:
        num += 1
        print(f"x = {num}  ",end = "")
        num = math.log(num)
        print(f"log(x) = {num}")
    else:
        print(f"x = {num}  ", end="")
        num = math.log(num)
        print(f"log(x) = {num}")
    