# 4875
from collections import deque
def bfs(start_pos):
    Q = deque()
    visited = [[False]*N for _ in range(N)]
    Q.append(start_pos)
    visited[start_pos[0]][start_pos[1]]= True
    while Q:
        r, c = Q.popleft()
        if maze[r][c] == '3':
            return 1
        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and maze[nr][nc] != '1':
                Q.append((nr, nc))
                visited[nr][nc]= True
    return 0
            
            
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                print(f'#{tc} {bfs((i,j))}')
                break
            
# 시간제한 너무 빡빡한거 아냐?