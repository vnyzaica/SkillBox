import random
def rock_paper_scissors():
    print("Добро пожаловать в игру Камень, ножницы, бумага")
    print("Ваш выбор")
    print("1. Камень")
    print("2. Ножницы")
    print("3. Бумага")
    x = int(input())
    robot = random.randint(1,3)
    if robot == x:
        print("Ничья")
    elif x == 1:
        if robot == 2 :
            print("Ты выиграл")
        else:
            print("Ты проиграл")
    elif x == 2:
        if robot == 3 :
            print("Ты выиграл")
        else:
            print("Ты проиграл")
    elif x == 3:
        if robot == 1 :
            print("Ты выиграл")
        else:
            print("Ты проиграл")
    mainMenu()

def rock_paper_scissors2():
    print("Добро пожаловать в игру Камень, ножницы, бумага")
    print("Ваш выбор")
    print("1. Камень")
    print("2. Ножницы")
    print("3. Бумага")
    input()
    z = ["Ты выиграл!","Ты проиграл!","Ничья!"]
    print(random.choice(z))
    mainMenu()

def guess_the_number():
    number = random.randint(0,10000)
    print("Игра Угадай число.")
    print("Тебе всего лишь необходимо указать число от 0 до 10000. Простая задача не так-ли?")
    count = 0
    z = -1
    print(number)
    while z != number:
        count += 1
        print(f"{count} попытка")
        z = int(input())
        if z > number:
            print("Не так много, возьми поменьше")
        elif z < number:
            print("Я не загадываю такие маленькие числа. Бери выше!")

    print(f"Ты угадал число {number} с {count} попытки.")
    mainMenu()

def mainMenu():
    print("Привет! Добро пожаловать в нашу игру. Пока что здесь всего 2 игры, но скоро будут обновления")
    print("\nВыберите игру")
    print("1. Камень ножницы бумага")
    print("2. Угадай число")
    print("3. Альтернативная версия 1 игры")
    choose = int(input())
    if choose == 1:
        rock_paper_scissors()
    elif choose == 2:
        guess_the_number()
    elif choose == 3:
        rock_paper_scissors2()
    else:
        print("Некорректный ввод. Попробуйте ещё раз.")
        mainMenu()

mainMenu()