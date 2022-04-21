people = 0
for n in range(11):
  number = int(input("Введите номер "))
  if number > 0 and number % 2 == 0:
    people += 1
print(f"Всего {people} человек, подходящих под требования")