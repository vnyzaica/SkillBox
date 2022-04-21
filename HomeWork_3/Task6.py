import random

first = random.randint(1, 6)
second = random.randint(1, 6) 
print(first)
print(second)
if first >= second:
  sum = (first - second) * 1000
  print(f"Костя задолжал {sum}$")
else:
  sum = (second + first) * 1000
  print(f"Владелец должен выплатить {sum}$")
  