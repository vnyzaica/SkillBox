how_much = int(input("Введите количество чисел "))
sum = 0
for i in range(how_much):
    prime_number = True
    number = int(input("Введите число ---> "))
    for n in range(2,number):
        if number % n == 0:
            prime_number = False

    if prime_number == True:
        sum += 1

print(f"Всего {sum} простых чисел")
