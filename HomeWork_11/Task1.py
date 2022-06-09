def summa_n (n):
    sum = 0
    for i in range(n):
        sum += i
    sum += n
    return sum

print(summa_n(5))