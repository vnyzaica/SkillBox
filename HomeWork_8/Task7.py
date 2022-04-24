text = input("Введите текст: ")
max = 0
length = 0
for symbol in text:
    if symbol == " ":
        length = 0
    else:
        length += 1
    if length > max:
        max = length

print(f"Самая длинное слово - {max}")