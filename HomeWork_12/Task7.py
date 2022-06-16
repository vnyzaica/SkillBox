#Знать бы ещё формулу подбора корней кубического уравнения, программа может и быстрее работала бы =)

def height(save):
    depth = 0
    can = -1000
    while depth < 3 :
        if save == depth ** 3 - 3 * (depth ** 2) - 12 * depth + 10:
            can = depth
        depth += 0.000000001
        print(depth, can)
    return can

print(height(0.01))