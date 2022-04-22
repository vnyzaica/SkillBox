boys = int(input("Введите количество мальчиков: "))
girls = int(input("Введите количество девушек: "))
if boys > girls * 2 or girls > boys * 2:
    print("Нет решения")
else:
    while boys != girls:
        if boys > girls:
            print("BGB",end="")
            boys -= 2
            girls -= 1
            last = True
        elif girls > boys:
            print("GBG",end="")
            boys -= 1
            girls -= 2
            last = False
        else:
            print("Error")
    while boys != 0:
        print("BG",end ="")
        boys -=1