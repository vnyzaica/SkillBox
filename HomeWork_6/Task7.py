#a = int(input("Введите первое число: "))
#b = int(input("Введите второе число: "))
#all_sum = 0
#counter = 0

#for n in range(a,b+1):
#  if n % 3 == 0:
#    counter += 1
#    all_sum += n

#average = all_sum / counter
#print(f"Среднее арифметическое - {average}")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
all_sum = 0
counter = 0

number = False

for n in range(a,b+1):
  if n % 3 == 0:
    counter += 1
    all_sum += n
    number = True
    
if number == True:
  if counter == 0:
    print(f"Среднее арифметическое - 0")
  else:
    average = all_sum / counter
    print(f"Среднее арифметическое - {average}")

else:
  print("Не было чисел подходящих под условие.")