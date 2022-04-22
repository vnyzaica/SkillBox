debtor = int(input("Введите количество должников: "))
sum = 0
for n in range(0,debtor,5):
    print(f"Должник с номером {n}")
    debt = int(input("Сколько он должен? "))
    sum += debt

print(f"Общая сумма долга {sum}.")