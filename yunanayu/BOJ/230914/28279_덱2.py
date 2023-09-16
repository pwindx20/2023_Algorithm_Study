from collections import deque
import sys

Q = deque([])
N = int(input())
for _ in range(N):
    T = sys.stdin.readline().split()
    # print(T)
    if T[0] == '1':
        Q.appendleft(int(T[1]))
    elif T[0] == '2':
        Q.append(int(T[1]))
    elif T[0] == '3':
        if Q:
            v = Q.popleft()
            print(v)
        else:
            print(-1)
    elif T[0] == '4':
        if Q:
            v = Q.pop()
            print(v)
        else:
            print(-1)
    elif T[0] == '5':
        print(len(Q))
    elif T[0] == '6':
        if Q:
            print(0)
        else:
            print(1)
    elif T[0] == '7':
        if Q:
            print(Q[0])
        else:
            print(-1)
    elif T[0] == '8':
        if Q:
            print(Q[-1])
        else:
            print(-1)
    # print(Q)