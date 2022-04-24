movement = True
X = 8
Y = 10
size_x = 15
size_y = 20

while movement == True:
    move = input(f"Марсоход находится на позиции {X}, {Y}. Куда движемся дальше? ")
    move = move.lower()
    if move == "w":
        X += 1
    elif move == "s":
        X -= 1
    elif move == "a":
        Y -= 1
    elif move == "d":
        Y += 1
    else:
        print("Введена неизвестная команда. Конец программы.")
        movement = False

    if X > size_x:
        X = size_x
    if X < 0:
        X = 0
    if Y > size_y:
        Y = size_y
    if Y < 0:
        Y = 0