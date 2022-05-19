def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

sum=0
user_number = int(input("До какого факториала будем искать сумму? "))
for i in range(user_number):
    i += 1
    sum += factorial(i)
    if i != user_number:
        print(f"{i}! + ",end = "")
    else:
        print(f"{i}! = ",end = "")
print(sum)