def NOD (first,second):
    for i in range(first+1):
        if i != 0:
            if first % i == 0 and second % i == 0:
                bigger = i
    return bigger

print(NOD(10,5))