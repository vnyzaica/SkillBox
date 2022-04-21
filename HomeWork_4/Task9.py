salary = int(input("Введите зарплату: "))

if salary < 10000:
  tax = salary * 0.13
else:
  tax = 10000*0.13
  if salary < 50000:
    tax = tax + (salary - 10000) * 0.2
  else:
    tax = tax + 40000*0.2
    tax = tax + (salary - 50000) * 0.2

print(f"Итого налог: {tax}")
