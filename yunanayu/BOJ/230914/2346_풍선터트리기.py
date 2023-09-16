from collections import deque

N = int(input())
lst = list(enumerate(map(int, input().split())))
Q = deque(lst)
result = []
while Q:
    idx, v = Q.popleft()
    result.append(idx+1)
    if v > 0:
        Q.rotate(-(v-1))
    elif v < 0:
        Q.rotate(-v)
print(*result)