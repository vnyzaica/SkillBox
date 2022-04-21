car_mileage = int(input("Введите пробег: "))
date = int(input("Введите число: "))
time=car_mileage
defect = car_mileage % 10
time = time // 10
defect = defect + time % 10
time = time // 10
defect = defect + time
del time

if defect == date:
  print("Сброс.")
  print("Пробег: 0")
else:
  print(f"Пробег: {car_mileage}")
  