russian = int(input("Введите количество баллов по русскому языку: "))
math = int(input("Введите количество баллов по математике: "))
informatics = int(input("Введите количество баллов по информатике: "))
amount = russian + math + informatics
if amount >= 270:
  print("Поздравляю, ты поступил на бюджет!")
else:
  print("К сожалению, ты не прошёл на бюджет.")