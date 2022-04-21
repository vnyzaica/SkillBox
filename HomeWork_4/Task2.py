first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

if first > second and first > third:
  print("Самое большое первое число")
elif second > first and second > third:
  print("Второе число самое большое")
elif third > first and third > second:
  print("Третье число самое большое")
else:
  print("Какие-то числа совпадают... ")