from collections import deque
from sys import stdin
input = stdin.readline


def searIdx():
    global save
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] != -1 and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    if save < cnt:
        save = cnt

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    while q:
        i, j = q.popleft()
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] != -1:
                visited[ni][nj] = True
                q.append((ni, nj))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_n = 0
min_n = 10000000
save = 0
for i in range(N):
    for j in range(N):
        if max_n < arr[i][j]:
            max_n = arr[i][j]
        if min_n > arr[i][j]:
            min_n = arr[i][j]

for i in range(min_n-1, max_n+1):
    visited = [[False] * N for _ in range(N)]
    for j in range(N):
        for k in range(N):
            if arr[j][k] <= i:
                arr[j][k] = -1
    searIdx()
print(save)