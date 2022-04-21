number = int(input("Какое число загадываем? "))
answer = "q"
n=0
while number != answer :
  n += 1
  answer = int(input("Введите число "))
  if number == answer:
    break
  elif number > answer:
    print("Возьми больше")
  else:
    print("Бери ниже")
print(f"Вы угадали число за {n} попыток")
