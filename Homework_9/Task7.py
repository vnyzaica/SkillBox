how_many = int(input("Из скольки чисел будем искать наибольшее? "))
big_sum = 0
for i in range(how_many):
    n = int(input("введите число "))
    sum = 0
    time_number = n
    while (n > 0):
        remain = n % 10
        sum = sum + remain
        n = n // 10
    # print(sum)
    if sum > big_sum:
        big_sum = sum
        number = time_number
print(f"Наибольшее число {number}")