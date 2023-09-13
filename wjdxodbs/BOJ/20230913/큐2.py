from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())
q = deque()
d = {
    'push': lambda x: q.append(x),
    'front': lambda: q[0] if q else -1,
    'back': lambda: q[-1] if q else -1,
    'empty': lambda: 0 if q else 1,
    'size': lambda: len(q),
    'pop': lambda: q.popleft() if q else -1
}

for i in range(N):
    m = list(input().split())
    if m[0] == 'push':
        d[m[0]](m[1])
    else:
        print(d[m[0]]())