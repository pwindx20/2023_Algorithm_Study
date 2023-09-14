from collections import deque

N, M = map(int, input().split())
q = deque()
q1 = deque()
for i in range(1, N+1):
    q.append(i)
n = M - 1
print('<', end='')
while q:
    for i in range(M-1):
        q.append(q.popleft())
    q1.append(str(q.popleft()))
print(', '.join(q1), end='')
print('>')