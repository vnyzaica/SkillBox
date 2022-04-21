budget = int(input("Введите стоимость: "))
square = int(input("Введите площадь: "))

if (square >= 100 and budget <= 10000000) or (square >= 80 and budget <= 7000000):
  print("Давайте возьмём эту квартиру")
else:
  print("Необходимо найти другую квартиру")
  