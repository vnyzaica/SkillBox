def count_letter(what,text):
    sum = 0
    for n in text:
        if n == what:
            sum += 1
    return sum
text = input("Введите текст для работы. ")
letter = input("Введите символ для подсчёта. ")
count = count_letter(letter, text)
print(count)
