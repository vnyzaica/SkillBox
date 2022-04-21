number = int(input("Какое число загадываем? "))
x = 0
z=64
a = z
n=1
f=0
while x != number:
  answer_question = int(input(f"Ваше число больше {a} "))
  if answer_question == 1:
    x = a
    break  
  elif answer_question == 2:
    print("Число больше")
    f += z    
  else:
    print("Число меньше")
  n += 1
  z = z / 2 
  a = int(z + f)
  x = a
  
print(f"Это число {x}")
  