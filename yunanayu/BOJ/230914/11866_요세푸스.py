from collections import deque
N, K = map(int,input().split())
lst = [(i+1) for i in range(N)]
Q = deque(lst)
result = []
while Q:
    Q.rotate(-(K-1))
    result.append(str(Q.popleft()))

print('<'+', '.join(result)+'>')
