lvl = int(1)
xp = int(input("Введите количество опыта: "))
if xp >= 1000 and xp < 2500:
  lvl = 2
elif xp >= 2500 and xp < 5000:
  lvl = 3
elif xp >= 5000:
  lvl = 4
print("Ваш уровень: ", lvl)