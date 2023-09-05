angle_l = []

for _ in range(3):
    angle_l.append(int(input()))

# print(angle_l)
if sum(angle_l) == 180:
    if angle_l[0] == angle_l[1] == angle_l[2]:
        print('Equilateral')
    elif angle_l[0] != angle_l[1] and angle_l[1] != angle_l[2] and angle_l[0] != angle_l[2]:
        print('Scalene')
    else:
        print('Isosceles')
else:
    print('Error')
