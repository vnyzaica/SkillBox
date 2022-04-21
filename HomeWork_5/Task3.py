x = True
while x == True:
  number = str(input("Введите число "))
  length = int(len(number))
  if length == 1:
    print(f"В числе {length} знак.")
  elif length == 2 or length == 3 or length == 4:
    print(f"В числе {length} знака.")
  else:
    print(f"В числе {length} знаков.")
  
