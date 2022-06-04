size = float(input("Введите вес скачиваемого файла "))
speed = float(input("Введите скорость скачивания "))
download = 0
second = 0
while download < size :
    second += 1
    download += speed
    percent = download / (size / 100)
    if percent > 100:
        percent = 100
        download = size
    print(f"Прошло {second} секунд. Скачано {download} из {size}. ({percent}%)")