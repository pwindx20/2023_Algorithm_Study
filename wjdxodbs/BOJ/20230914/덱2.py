from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())
dq = deque()
m = {
    '1': lambda x: dq.appendleft(x),
    '2': lambda x: dq.append(x),
    '3': lambda: print(dq.popleft() if dq else -1),
    '4': lambda: print(dq.pop() if dq else -1),
    '5': lambda: print(len(dq)),
    '6': lambda: print(0 if dq else 1),
    '7': lambda: print(dq[0] if dq else -1),
    '8': lambda: print(dq[-1] if dq else -1)
}

for i in range(N):
    a = list(input().split())
    if a[0] in {'1', '2'}:
        m[a[0]](a[1])
    else:
        m[a[0]]()
