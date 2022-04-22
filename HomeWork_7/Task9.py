# numerator = 1
# denominator = 1
# x = int(input("Введите значение x --> "))
# for n in range(1,64,2):
#     numerator *= (x - n)
#
# for n in range(2,65,2):
#     denominator *= (x-n)
#
# res = numerator / denominator
# print(f"Результат равен {res}")

numenator = 1
denominator = 1
x = int(input("Х --> "))
num = 0
den = 1
for n in range(6):
    num += 2**n
    den += 2**n
    numenator *= (x-num)
    denominator *= (x-den)

res = numenator / denominator
print(f"Результат равен {res}")