from collections import deque
import sys
input = sys.stdin.readline

def island(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    while q:
        i, j = q.popleft()
        for di, dj in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
            ni, nj = i+di, j+dj
            if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj] and arr[ni][nj]:
                visited[ni][nj] = True
                q.append((ni, nj))


while True:
    w, h = map(int, input().split())
    if not w and not h:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] and not visited[i][j]:
                cnt += 1
                island(i, j)
    print(cnt)