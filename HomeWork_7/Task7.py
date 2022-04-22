educational_grant = int(input("Введите размер стипендии --> "))
expenses = int(input("Введите расходы на проживание --> "))
sum = 0

for i in range(10):
    sum += expenses * (1.03 ** i) - educational_grant

print(f"У родителей необходимо попросить {sum} рублей")