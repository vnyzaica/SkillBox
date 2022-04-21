number = 50
counter = 0
while number != 0:
  number = int(input("Введите число дней: "))
  if number == 0:
    break
  if number % 2 == 0:
    counter = counter + 1

print(f"Введено {counter} четных чисел.")
  