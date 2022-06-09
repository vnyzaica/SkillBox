def check(x,y):
    global verify
    if -1 <= x <= 1 and -1 <= y <= 1 :
        print("Монетка где-то рядом")
        verify = True
    else:
        print("Монетки нет в области")

verify = False
while verify == False:
    x = float(input("Введите Х "))
    y = float(input("Введите Y "))
    check(x,y)

