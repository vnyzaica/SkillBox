a = int(input("Введите значение A "))
b = int(input("Введите значение B "))
c = int(input("Введите значение С "))
sum = 0
x = 0
for n in range(a,b+1):
    if n % c == 0:
        sum += n
        x += 1

print(sum / x)