high = int(input("Введите высоту: "))
long= int(input("Введите длину: "))
for h in range(high):
    for l in range(long):
        if (h == 0) or (h == high-1):
            print("-", end = "")
        else:
            if (l == 0) or (l == long-1):
                print("|", end = "")
            else:
                print(" ", end = "")
    print()