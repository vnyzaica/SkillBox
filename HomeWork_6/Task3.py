sum_salary = 0
for n in range(13):
  salary = int(input("Введите ЗП за месяц "))
  sum_salary += salary
average_salary = sum_salary / 12 
print(f"Средняя зарплата у сотрудника --> {average_salary}")