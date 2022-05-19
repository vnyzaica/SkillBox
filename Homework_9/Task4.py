size = int(input("Введите размер креста -- > "))
for row in range(size):
    for col in range(size):
        if (col == row) or (col == size - 1 -row):
            print("^", end ="")
        else:
            print(" ", end="")
    print()