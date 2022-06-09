def sum_num(num):
    sum = 0
    while (num != 0):
        sum = sum + num % 10
        num = num // 10
    print(sum)

def max_number(num):
    sum = 0
    while (num != 0):
        if sum < (num % 10):
            sum = num % 10
        num = num // 10
    print(sum)

def min_number(num):
    sum = 10
    while (num != 0):
        if sum > (num % 10):
            sum = num % 10
        num = num // 10
    print(sum)

def calculate(number,move):
    if move == 1 :
        sum_num(number)
    elif move == 2:
        max_number(number)
    elif move == 3:
        min_number(number)
    else:
        print("Некорректный ввод")

num = int(input("Введите число "))
mov = int(input("Введите действие "))
calculate(num, mov)
