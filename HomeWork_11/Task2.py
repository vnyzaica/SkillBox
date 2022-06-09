def positive():
    print("Положительное")

def negative():
    print("Отрицательное")

def test():
    x = int(input("Введите число "))
    if x < 0 :
        negative()
    else:
        positive()

test()