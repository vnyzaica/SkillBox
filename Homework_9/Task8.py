size = int(input("Введите размер пирамидки "))
long = int((size - 1) * 2 + 1)
for i in range(size):
    time = int((long - 2*i + 1) / 2)
    print(" "*time + "#" * (2*i+1) + " "*time)