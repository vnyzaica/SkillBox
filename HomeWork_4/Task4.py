rang = int(input("Введите место в списке поступающих: "))
scores = int(input("Введите количество баллов за экзамены: "))
if rangs < 11 :
  print("Поздравляем вы поступили!")
  if scores >= 290:
    print("Бонусом вам будет начисляться стипендия.")
  else:
    print("Но вам не хватило баллов для стипендии.")
else:
  print("К сожалению вы не поступили.")

