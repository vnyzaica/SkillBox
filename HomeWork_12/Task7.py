#Знать бы ещё формулу подбора корней кубического уравнения, программа может и быстрее работала бы =)
# def height(save):
#     depth = 0
#     can = -1000
#     while depth < 3 :
#         if save == depth ** 3 - 3 * (depth ** 2) - 12 * depth + 10:
#             can = depth
#         depth += 0.000000001
#         print(depth, can)
#     return can
#
# print(height(0.01))

d_from = 0
d_to = 4
max_danger = float(input("Введите максимально допустимый уровень опасности: "))
depth = d_from + (d_to - d_from) / 2
danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10
if max_danger < 0:
    print("Ошибка")
else:
    print(f"Depth: {depth}  Danger: {danger}")
    while abs(danger) > max_danger:
        if danger > 0:
            d_from = depth
        else:
            d_to = depth

        depth = d_from + (d_to - d_from) / 2
        danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10