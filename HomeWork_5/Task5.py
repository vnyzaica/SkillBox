number = int(input("Введите номер билета "))
first = number // 100000
first = (number // 10000) % 10 + first
first = (number // 1000) % 10 + first

second = (number // 100) % 10 
second = (number // 10) % 10 + second
second = number % 10 + second

if first == second:
  print("Это счастливый билет!")
else:
  print("Это не счастливый билет...")
  