#Функция определния окончаний!
def many(m, predefined=''):
    d = [
        ['дойт', 'дойта','дойтов'],
        ['майт', 'майта', 'майтов'],
        ['гран','грана', 'кловы'],
        ['пеннивейт', 'пеннивейта', 'пеннивейтов']
    ]
    res = predefined
    if m[0]%10== 1:
        res += str(m[0]) + ' ' + d[1][0]
    elif m[0]%10==2 or 3 or 4 :
        res += str(m[0]) + ' ' + d[1][1]
    elif m[0]%10==5 or 6 or 7 or 8 or 9:
        res += str(m[0]) + ' ' + d[1][2]
    elif m[0]%10==0:
        res += str(m[0]) + ' ' + d[1][2]
    elif m[0]%10==11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19:
        res += str(m[0]) + ' ' + d[1][2]
    res += ' '
    if m[1]%10== 1:
        res += str(m[1]) + ' ' + d[2][0]
    elif m[1]%10==2 or 3 or 4:
        res += str(m[1]) + ' ' + d[2][1]
    elif m[1]%10==5 or 6 or 7 or 8 or 9:
        res += str(m[1]) + ' ' + d[2][2]
    elif m[1]%10==0:
        res += str(m[1]) + ' ' + d[2][2]
    elif m[1]%10==11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19:
        res += str(m[1]) + ' ' + d[2][2]
    res += ' '
    if m[2]%10== 1:
        res += str(m[2]) + ' ' + d[3][0]
    elif m[2]%10==2 or 3 or 4:
        res += str(m[2]) + ' ' + d[3][1]
    elif m[2]%10==5 or 6 or 7 or 8 or 9:
        res += str(m[2]) + ' ' + d[3][2]
    elif m[2]%10==0:
        res += str(m[2]) + ' ' + d[2][3]
    elif m[1]%10==11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19:
        res += str(m[2
                     ]) + ' ' + d[2][3]
    print(res)
#Функция перевода значения в наименьшую единицу!
def translation(m):
    n = m [0] * 480 + m [1]*24 + m [2]
    return n
#Функция перевода значения в исходный вид!
def back(n):
    a0 = n %24
    a1 = (n//24)%20
    a2 = n//24//20
    a = (a2,a1,a0)
    return a
#Функция проверки допустимого диапазона!
def restriction(m):
    if translation(m) > 92160:
        return False
    return True
#Функция, выполняющая операцию сложение!
def amount(a):
    while True:
        plus = enter ()
        summ = back(translation(a) + translation(plus))
        if restriction(summ) == False:
            print ('Значение выходит за пределы допустимого диапазона')
            continue
        else:
            print ('Сумма равна = ', summ [0], ' гранов', summ [1], ' майтов', summ [2], ' дойтов')
        break
    return(summ)
#Функция,выполняющая операцию вычитание!
def subtraction(znach):
    while True:
        minus = enter ()
        if translation(znach)<translation(minus):
            print('второе значение больше первого,операция невозможна,повторите ввод')
            continue
        else:
            vich = back(translation(znach) - translation(minus))
        if restriction(vich) == False:
            print ('Значение выходит за пределы допустимого диапазона')
            continue
        else:
            print ('Разность равна = ', vich [0], ' гранов', vich [1], ' майтов', vich [2], ' дойтов')
        break
    return(vich)
#Функция, выполняющая операцию сравнение!
def comparison(znach):
    sr = enter ()
    if translation(sr) > translation(znach):
        print ('Введенное значение больше предыдущего')
    elif translation(sr) == translation(znach):
        print ('Введенное значение равно предыдущему')
    else:
        print ('Введенное значение меньше предыдущего')
    print (chr (13))
#Функция, выполняющая операцию умножение!
def multiplication(znach):
    while True:
        while True:
            number = input ('Введите множитель: ')
            if not number.isdigit():
                print ("Ошибка: требуется ввести цифровое значение")
                continue
            break
        pr = back(translation(znach)*int(number))
        if restriction(pr) == False:
            print ('Значение выходит за пределы допустимого диапазона')
            continue
        else:
            print ('Произведение равно = ', pr [0], ' гранов ', pr [1], ' майтов', pr [2], ' дойтов ')
        break
    return(pr)
#Функция, выполняющая операцию деление!
def division(znach):
    while True:
        while True:
            number = input ('Введите делитель: ')
            if not number.isdigit():
                print ("Ошибка: требуется ввести цифровое значение")
                continue
            break
        ch = back(translation(znach)// int(number))
        if restriction(ch) == False:
            print ('Значение выходит за пределы допустимого диапазона')
            continue
        else:
            print ('Частное равно = ', ch [0], ' гранов', ch [1], ' майтов', ch [2], ' дойтов')
        break
    return(ch)
#Функция, вычисляющая дополнение до 1 пеннивейта!
def supplement(znach):
    if translation(znach)>11520:
        print('Введённое значение больше 1 пеннивейта')
    elif translation(znach) == 11520:
        print("Введенное значение равно одному пеннивейт")
    else:
        dop = back (11520 - translation(znach))
        print ('До 1 пеннивейта необходимо добавить: ', dop [0], ' гранов', dop [1], ' майтов', dop [2], ' дойтов')
        print (chr (13))
#Функция, выполняющая перевод в миллиграммы, сы и периоты!
def conversion(znach):
    k = translation(znach) * 0.135
    lt = k
    si = k / 0.5
    kub = k / 0.00675
    print ('\n сы = ', si, '\n периоты = ', kub)
    print (chr (13))
#Функция, выполняющая ввод данных (гранов,майтов,дойтов)!
def enter ():
    while True:
        while True:
            ocm = input ('Введите количество гранов ')
            if not ocm.isdigit():
                print ("Ошибка: требуется ввести цифровое значение")
                continue
            break
        while True:
            gran = input('Введите количество майтов ')
            if not gran.isdigit():
                print("Ошибка: требуется ввести цифровое значение")
                continue
            break
        while True:
            stak = input('Введите количество дойтов ')
            if not stak.isdigit():
                print("Ошибка: требуется ввести цифровое значение")
                continue
            break
        znach = (int(ocm), int(gran), int(stak))
        if restriction(znach) == False:
            print('Значение выходит за пределы допустимого диапазона')
            continue
        else:
            print('Введенное число: ', znach[0], ' гранов', znach[1], ' майтов', znach[2], ' дойтов')
            break
    return znach
#Функция вывода пункта главного меню: операции над значением!
def operation(znach):
    punktik = '0'
    while (punktik != 'Q' and punktik != 'q'):
        if punktik == '0':
            print ('\n ',
                   '\n    Меню операций: ',
                   '\n [+] - Сложение',
                   '\n [-] - Вычитание',
                   '\n [&] - Сравнение двух значений',
                   '\n [*] - Умножение',
                   '\n [/] - Деление',
                   '\n [Q] - Выход из меню операций')
        elif punktik == '+':  znach = amount(znach)
        elif punktik == '-':  znach = subtraction(znach)
        elif punktik == '&':  comparison(znach)
        elif punktik == '*':  znach = multiplication(znach)
        elif punktik == '/':  znach = division (znach)
        else:
            print("Такой команды нет")
        punktik = (input("Введите команду с операцией: "))
    return znach
#Функция вывода главного меню!
def main():
    print("Программа подсчета массы в тройской системе мер")
    punkt = '0'
    while (punkt != 'Q' and punkt != 'q'):
        if punkt == '0':
            print ('\n ',
                   '\n    Главное меню: ',
                   '\n [E] - Ввод значения',
                   '\n [O] - Операции над значением',
                   '\n [S] - Дополнение до 1 пеннивейта',
                   '\n [C] - Преобразование в сы, периоты',
                   '\n [Q] - Выход')
        elif punkt == 'E' or punkt == 'e':  znach = enter ()
        elif punkt == 'O' or punkt == 'o':  znach = operation(znach)
        elif punkt == 'S' or punkt == 's':  supplement(znach)
        elif punkt == 'C' or punkt == 'c':  conversion(znach)
        else:
            print ("Такой команды нет.")
        punkt = (input ("Введите команду: "))
# Запуск главной функции
if __name__ == '__main__':
              main ()
