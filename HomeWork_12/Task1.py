#Вопрос, про второй пример. Если вбивать второй пример, то выходит бесконечный результат, что не совсем корректно, а решить данную проблему самостоятельно не получилось.

def GoToE(number):
    z = 0
    while number >= 10 or number < 1 :
        if number < 1:
            number *= 10
            z -= 1
        else:
            number /= 10
            z += 1
    return (number, z)

x = float(input("Введите число "))
x = GoToE(x)

print(f"Начальное число равно {x[0]} * 10 ^ {x[1]}")