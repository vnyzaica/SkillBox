
N = int(input("До какого числа будем искать факториал? "))
result = 1
for n in range(1,N+1):
  result *= n 
  print(f"{n}! = {result}")

