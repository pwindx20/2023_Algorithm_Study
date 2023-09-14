from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())
lst = deque(map(int, input().split()))
for i in range(N):
    lst[i] = (lst[i], i+1)
for _ in range(N):
    a, b = lst.popleft()
    print(b)
    if lst:
        if a >= 0:
            for i in range(a - 1):
                lst.append(lst.popleft())
        else:
            for i in range(-a):
                lst.appendleft(lst.pop())
