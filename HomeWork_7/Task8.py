n = int(input("Введите натуральное число N --> "))
sum = 0
for i in range(n+1):
    sum += ((-1) ** i) * (1/(2**i))
print(sum)