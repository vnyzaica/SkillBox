def amplitude(start,stop):
    how_much = 0
    while start > stop:
        start *= 0.916
        how_much += 1
    return how_much

start = float(input("Введите начальную амплитуду: "))
stop = float(input("Введите амплитуду остановки: "))
print(f"Маятник будет считаться остановившимся через {amplitude(start, stop)} колебаний")