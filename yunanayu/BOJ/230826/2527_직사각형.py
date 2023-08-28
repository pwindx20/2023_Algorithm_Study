import sys
sys.stdin = open('2477.txt','r')

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    if p1 < x2 or q1 < y2 or p2 < x1 or q2 < y1:
        print('d')
        continue
    elif (x1 == x2 and y1 == y2) or (x1==p2 and y1==q2) or (x2 == p1 and y2 == q1) or (p1 == p2 and q1 == q2):
        print('c')
        continue
    elif (q1 == y2) or (p1 == x2) or (x1 == p2) or (y1 == q2):
        print('b')
        continue
    else:
        print('a')
