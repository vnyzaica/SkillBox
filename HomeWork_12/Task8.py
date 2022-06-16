def func(accuracy, number):
    sum = 1
    sum2=1000000000000
    count = 0
    while accuracy < 1:
        count += 1
        accuracy *= 10
    for i in range(1,100):

        factorial = 1
        for n in range(2, 2 * i + 1):
            factorial *= n

        sum += ((-1) ** i) * (number ** (2 * i)) / factorial
        if round(sum, count) == sum2:
            break
        sum2 = round(sum, count)

    return sum

accuracy = float(input("Введите точность: "))
num = int(input("Введите х: "))
print(f"Сумма ряда - {func(accuracy, num)}")
