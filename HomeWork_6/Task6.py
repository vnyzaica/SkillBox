N = int(input("Cколько человек в классе? "))
excellent_student = 0
good_guy = 0
acceptable_guy = 0

for n in range(N):
  result = int(input("Введите оценку "))
  if result == 3:
    acceptable_guy += 1
  elif result == 4:
    good_guy += 1
  else:
    excellent_student += 1

if excellent_student < acceptable_guy > good_guy :
  print("У большинства тройки. Надо поднимать эту тему.")
elif excellent_student < good_guy > acceptable_guy:
  print("Большинство хорошисты.")
elif good_guy < excellent_student > acceptable_guy :
  print("Молодцы! У большиства пятёрки!")
else:
  print("Я сломалься")
