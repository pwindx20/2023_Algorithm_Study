# 10966 
# 제한시간 너무 빡빡해
from collections import deque
def water():
    Q = deque()
    
    for i in range(N):
        for j in range(M):
            if basic[i][j] =='W':
                Q.append((i, j, 0))
    # print(Q)

    while Q:
        r, c, d = Q.popleft()
        if basic[r][c] =='L' and visited[r][c]==0:
            visited[r][c] = d
            
        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr, nc = r+dr, c+dc
            if 0<=nr<N and 0<=nc<M and visited[nr][nc]==0 and basic[nr][nc]=='L':
                Q.append((nr, nc, d+1))
            
            
T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    basic = [input().strip() for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    water()
    # print(visited)
    total = 0
    for row in visited:
        total += sum(row)
    print(f'#{tc} {total}')