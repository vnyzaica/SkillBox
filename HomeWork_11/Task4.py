def change(number):
    sum =str("")
    while (number != 0):
        z = number % 10
        sum += str(z)
        number = number // 10
    print(sum)

num = 1
while num != 0:
    num = int(input("Введите число для переворачивания: "))
    change(num)

print("Работа программы завершена. Спасибо.")