def versa(num):
    number = 0
    while num >= 1:
        num = int(num)
        number *= 10
        number = (num % 10) + number
        num /= 10
    return number

first = int(input("Введите первое число "))
second = int(input("Введите второе число "))
first_versa = versa(first)
second_versa = versa(second)
sum = first_versa + second_versa
sum_versa = versa(sum)
print(f"Первое число наоборот {first_versa}")
print(f"Второе число наоборот {second_versa}")
print(f"Сумма {sum}")
print(f"Сумма наоборот - {sum_versa}")