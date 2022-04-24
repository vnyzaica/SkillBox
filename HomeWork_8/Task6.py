text = input("Введите шифр: ")
max = 0
time = 0
for symbol in text:
    if symbol == "s":
        time += 1
    else:
        time = 0
    if time > max:
        max = time

print(f"Самая длинная последовательность - {max}")
