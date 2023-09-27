from sys import stdin
input = stdin.readline

def bfs(i, j):
    q = [(i, j)]
    visited = [[-1] * M for _ in range(N)]
    visited[i][j] = 0
    while q:
        i, j = q.pop(0)
        if i == N-1 and j == M-1:
            return visited[i][j] + 1
        for di, dj in ((-1, 0), (0, 1), (0, -1), (1, 0)):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == '1' and visited[ni][nj] == -1:
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni, nj))
    return 0


N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
print(bfs(0, 0))