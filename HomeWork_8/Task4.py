row = int(input("Введите количество рядов: "))
seat = int(input("Введите количество сидений: "))
free = int(input("Сколько метров между креслами? "))
print("Сцена")
for i in range(row):
    print("=" * seat + "*" * free + "=" * seat)