name = input("Введите имя должника: ")
debt = int(input("Сколько должен клиент? "))
pay = 0
while debt > pay :
  print(f"{name}, ваша задолженность составляет {debt} рублей.")
  pay = int(input("Сколько денег вы сможете внести сейчас? "))
  if pay >= debt:
    print(f"Отлично {name}! Вы погасили долг.")
  else:
    print("Давайте попробуем внести сумму побольше? ")