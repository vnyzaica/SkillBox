def input_xy():
    meaning = float(input())
    while meaning > 8 or meaning < 1:
        print("За пределами доски. Попробуйте повторно.")
        meaning = float(input())
    return meaning

print("Программа написана из расчёта использования целых клеток от 1 до 8")
print("Введите местоположение коня")
x_now = input_xy()
y_now = input_xy()
print("\nВведите желаемое местоположение")
x_future = input_xy()
y_future= input_xy()
can = False


for i in range(-1,2,2):
    for x in range(2):
        z = x % 2
        x_maybe = x_now + (2 ** z * i)
        for y in range(2):
            if z == 0:
                if y == 0:
                    y_maybe = y_now - 2
                else:
                    y_maybe = y_now + 2
            if z == 1:
                if y == 0:
                    y_maybe = y_now - 1
                else:
                    y_maybe = y_now + 1
            if x_maybe == x_future and y_maybe == y_future:
                can = True

if can == True:
    print("Может")
else:
    print("Не может")