print("Начался 8-часовой рабочий день")
hour = 8
all_task = 0
go_to_shop = False
while hour != 0:
  print(f"{hour}-й час")
  task = int(input("Сколько задач будет решено? "))
  shop = int(input("Звонит жена. Взять трубку? "))
  if shop == 1:
    go_to_shop = True
  all_task += task
  hour -= 1
print(f"Рабочий день закончился. Всего выполнено задач: {all_task}")
if go_to_shop == True:
  print("Нужно зайти в магазин")

