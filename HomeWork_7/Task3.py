seconds = int(input("Сколько секунд будет разогреваться еда? "))
for second in range(seconds,0,-1):
    print(f"До конца разогрева продукта осталось {second} секунд")
    result = int(input("Оставляем разогреваться? "))
    if result == 1:
        break
        print(f"До конца таймера осталось {second}")

print("Ваша еда готова, осторожно горячo!")