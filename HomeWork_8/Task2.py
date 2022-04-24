success = int(0)
for pirates in range(11):
    word = input("Какое слово выкрикнул пират? ")
    word = word.lower()
    if word == "карамба":
        success += 1

print(f"Всего проходит {success} человек.")
