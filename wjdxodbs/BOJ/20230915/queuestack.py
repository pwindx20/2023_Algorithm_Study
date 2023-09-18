from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))
result = deque()
for i in range(N):
    if not A[i]:
        result.appendleft(B[i])
for i in range(M):
    result.append(C[i])
    print(result.popleft(), end=' ')