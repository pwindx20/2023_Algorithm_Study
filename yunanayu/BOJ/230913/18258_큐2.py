import sys
from collections import deque

N = int(input())
Q = deque([])
for _ in range(N):
    T = sys.stdin.readline().split()
    if T[0] == 'push':
        Q.append(T[1])
    elif T[0] == 'pop':
        if Q:
            v = Q.popleft()
            print(v)
        else:
            print(-1)
    elif T[0] == 'size':
        print(len(Q))
    elif T[0] == 'empty':
        if Q:
            print(0)
        else:
            print(1)
    elif T[0] == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)
    elif T[0] == 'back':
        if Q:
            print(Q[-1])
        else:
            print(-1)
