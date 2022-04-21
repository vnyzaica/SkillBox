violation = 0
for n in range(30,36):
  people = int(input(f"Сколько людей в {n}-м секторе? "))
  if people > 10:
    violation += 1
    print("Нарушение! Надо кого-то выгнать!")
  else:
    print("Всё в норме")
print(f"Количество нарушений: {violation}")
