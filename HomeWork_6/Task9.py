time_variable = 0
for n in range(11):
  salary = int(input("Введите сумму зарплаты --> "))
  if salary <= time_variable :
    print("Ваша зарплата не увеличивается от месяца к месяцу")
    break
  else:
    print("Ваша зарплата стала больше")
    time_variable = salary