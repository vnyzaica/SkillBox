def max_number(first,second):
    big = (first >= second) * first + (first < second) * second
    return big

first = float(input())
second = float(input())
third = float(input())
maxim = max_number(first,second)
maxim = max_number(maxim,third)
print(maxim)