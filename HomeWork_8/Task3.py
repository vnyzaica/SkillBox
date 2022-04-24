text = input("Введите некорректное сообщение -- > ")
number = 1
for letter in text:
    if letter == "*":
        print(f"Символ находится на {number} позиции.")
    else:
        number += 1