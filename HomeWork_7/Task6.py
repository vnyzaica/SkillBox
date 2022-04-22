length = int(input("Введите длину конверта в сантиметрах: "))
width = int(input("Введите ширину конверта в сантиметрах: "))
size_w = 12
size_l=12
bend = 0
while size_w > width:
    size_w /= 2
    bend += 1
while size_l > length:
    size_l /= 2
    bend += 1
print(f"Потребуется {bend} изгибов.")


