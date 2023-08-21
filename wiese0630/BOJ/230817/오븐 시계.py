A, B = map(int, input().split())
C = int(input())

min = B+C

if min < 60:
    print(A, min)

else:
    newmin = min % 60
    newh = A + (min//60)
    if newh >= 24:
        newh %= 24
    print(newh, newmin)
