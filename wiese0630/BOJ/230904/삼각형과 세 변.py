while True:
    X, Y, Z = map(int, input().split())
    if [X, Y, Z] == [0, 0, 0]:
        break

    if max([X, Y, Z]) >= sum([X, Y, Z]) - max([X, Y, Z]):
        print('Invalid')
    else:
        if X == Y == Z:
            print('Equilateral')
        elif X != Y and Y != Z and Z != X:
            print('Scalene')
        else:
            print('Isosceles')



