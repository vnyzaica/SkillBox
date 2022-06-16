# Не понял ни задание, ни предоставленную формулу...

credit = input("Введите сумму кредита ")
credit = credit.split("e")
credit = int(int(credit [0]) * 10 ** int(credit[1]))

year = int(input("На сколько лет выдан кредит? "))
procent = float(input("Сколько процентов годовых? "))
procent /= 100
K = (procent * ((1 + procent) ** year)) / (1 + procent) ** year - 1
A = credit * K
print(K)
print(A)