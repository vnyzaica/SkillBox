evaluation = 1
positive = 0
negative = 0
while evaluation != 0 :
  evaluation = int(input("Введите оценку приложению --> "))
  if evaluation > 0:
    positive = positive + 1
  if evaluation < 0:
    negative = negative + 1
print(f"Приложение оценивают так:  {positive} / {negative}")