size = int(input("Введите размер пирамидки "))
size += 1
long = int((size - 1) * 2 + 1)
sum = 1
for i in range(size):
    time = int((long - 2*i + 1) / 2)
    print("\t"*time, end = "")
    for n in range(i):
        print(f"{sum}" + "\t" * 2, end="")

        sum += 2
    print()