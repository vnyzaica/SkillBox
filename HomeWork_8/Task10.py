text = input("Введите шифр: ")
time = 0

for symbol in text:
    if time == 0:
        print(symbol,end="")
        time += 1
    else:
        time -= 1

text = text[::-1]

if len(text) % 2 == 1:
    time = 1
else:
    time = 0

for symbol in text:
    if time == 0:
        print(symbol,end="")
        time += 1
    else:
        time -= 1