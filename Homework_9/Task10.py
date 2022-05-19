height = int(input("Введите размер ямы --->  "))
for i in range(height):
    how_much = int(2 * (height - i))
    print(height, "." * how_much, height)