from collections import deque
from sys import stdin
input = stdin.readline


def searIdx():
    lst = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                lst.append((i, j))
    return lst


def bfs(lst):
    q = deque(lst)
    visited = [[-1] * M for _ in range(N)]
    for i, j in q:
        visited[i][j] = 0
    cnt = 0
    max_n = 0
    while q:
        i, j = q.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == -1 and arr[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    for i in range(N):
        cnt += visited[i].count(-1)
    if cnt > cntm:
        return -1
    else:
        for i in range(N):
            if max_n < max(visited[i]):
                max_n = max(visited[i])
        return max_n


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = cntm = 0

for i in range(N):
    cnt += arr[i].count(0)
    cntm += arr[i].count(-1)
if cnt:
    print(bfs(searIdx()))
else:
    print(0)