time = int(input("Введите время: "))

if (time >= 8 and time < 10) or (time >= 12 and time < 14) or (time >= 15 and time < 18) or (time >= 20 and time < 22):
  print("Посылку получить можно, но там возможно очередь 😀")
else:
  print("Попробуйте другое время для получения посылки")