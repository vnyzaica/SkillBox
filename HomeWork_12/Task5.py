def len_number(num):
    num_count = 0
    while num > 0:
        num_count += 1
        num = num // 10
    return num_count

def func (number,count):
    last_digit = number % 10
    first_digit = number // 10 ** (count - 1)
    between_digits = number % 10 ** (count - 1) // 10
    first_n = last_digit * 10 ** (count - 1) + between_digits * 10 + first_digit
    print(f"Изменённое число - {first_n}")
    return first_n


first_n = int(input("Введите первое число: "))
if len_number(first_n) < 3:
    print("В первом числе меньше трёх цифр.")
else:
    first_n = func(first_n,len_number(first_n))

    second_n = int(input("\nВведите второе число: "))
    second_num_count = len_number(second_n)
    if len_number(second_n) < 4:
        print("Во втором числе меньше четырёх цифр.")
    else:
        second_n = func(second_n, len_number(second_n))

        print('\nСумма чисел:', first_n + second_n)
