from collections import deque
import sys
input = sys.stdin.readline


def BFS(i, j):
    q = deque()
    q.append((i, j))
    cnt = 1
    while q:
        i, j = q.popleft()
        for di, dj in ((-1, 0), (0, 1), (0, -1), (1, 0)):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] == '1':
                cnt += 1
                q.append((ni, nj))
                visited[ni][nj] = True
    else:
        result.append(cnt)


def searIdx():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '1' and not visited[i][j]:
                cnt += 1
                visited[i][j] = True
                BFS(i, j)
    print(cnt)


N = int(input())
visited = [[False] * N for _ in range(N)]
arr = [list(input().rstrip()) for _ in range(N)]
result = []
searIdx()
print(*sorted(result), sep='\n')