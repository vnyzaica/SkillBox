#N = int(input("Сколько карточек в игре? "))
#x = list(range(1, N + 1))
#print (x)
#for n in range(N - 1):
#  card = int(input("Введите номер найденой карточки "))
#  x.remove(card)

#x = int(x[0])
#print(f"Не хватает карточки с номером {x}")


N = int(input("Сколько карточек в игре? "))
sum = 0
sum2 = 0
for n in range(1,N+1):
  sum += n

for n in range(N - 1):
  card = int(input("Введите номер найденой карточки "))
  sum2 += card

x = sum - sum2
print(f"Не хватает карточки с номером {x}")