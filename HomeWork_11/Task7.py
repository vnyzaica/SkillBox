def minimum(first,second):
    one = abs(first + second)
    two = abs(first - second)
    ret = (one - two) / 2
    return ret

print(minimum(5, 1))