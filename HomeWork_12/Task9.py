credit = input("Введите сумму кредита ")
credit = credit.split("e")
credit = int(int(credit [0]) * 10 ** int(credit[1]))

year = int(input("На сколько лет выдан кредит? "))
procent = float(input("Сколько процентов годовых? "))
procent /= 100
tr = True
for i in range(1,4):

    K = (procent * ((1 + procent) ** year)) / (1 + procent) ** year
    A = credit * K
    site_K = (procent) * ((1 + procent) ** year) / ((1 + procent) ** year - 1)
    print(f"Период {i}")
    print(f"Остаток долга: {credit}")
    print("K - ", K)
    print(f"Выплачено процентов {A}")
    if tr == True:
        proc = credit * site_K
        print("proc - ", proc)
        time = proc
        tr = False
    body = proc - A
    print(f"Выплачено тела кредита : {body}")
    credit -= body
    print()
print(f"Остаток долга - {credit}")
print("\n\n====================\n\n")

i = 4

year = year - 3 + int(input("На сколько лет продлевается договор?"))
procent = float(input("Увеличение ставки до "))
procent /= 100
tr = True
while credit > 1:
    K = (procent * ((1 + procent) ** year)) / (1 + procent) ** year
    A = credit * K
    site_K = (procent) * ((1 + procent) ** year) / ((1 + procent) ** year - 1)
    print(f"Период {i}")
    print(f"Остаток долга: {credit}")
    print("K - ", K)
    print(f"Выплачено процентов {A}")
    if tr == True:
        proc = credit * site_K
        print("proc - ", proc)
        time = proc
        tr = False
    body = proc - A
    print(f"Выплачено тела кредита : {body}")
    credit -= body
    print()
    i += 1

print(f"Осталось - {credit}")