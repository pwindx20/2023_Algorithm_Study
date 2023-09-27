# 2178
# 입력: N, M/ N개 줄 M개 정수
# 출력: 최소칸 수
def bfs():
    Q = [(0, 0, 1)]
    visited[0][0] = True
    while Q:
        i, j, cnt = Q.pop(0)
        if i==N-1 and j==M-1:
            return cnt
        for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]=='1' and not visited[ni][nj]:
                visited[ni][nj] = True
                Q.append((ni, nj, cnt+1))
    
N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

print(bfs())