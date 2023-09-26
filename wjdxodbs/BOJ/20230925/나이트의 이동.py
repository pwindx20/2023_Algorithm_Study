from collections import deque
import sys
input = sys.stdin.readline

def knight(i, j):
    q = deque()
    q.append((i, j))

    while q:
        i, j = q.popleft()
        for di, dj in ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)):
            ni, nj = i + di, j + dj
            if 0 <= ni < l and 0 <= nj < l and visited[ni][nj] == -1:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                if ni == t1 and nj == t2:
                    return visited[ni][nj]


for _ in range(int(input())):
    l = int(input())
    s1, s2 = map(int, input().split())
    t1, t2 = map(int, input().split())
    visited = [[-1] * l for _ in range(l)]
    visited[s1][s2] = 0
    if s1 == t1 and s2 == t2:
        print(0)
    else:
        print(knight(s1, s2))
