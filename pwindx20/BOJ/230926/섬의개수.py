# 4963
# 입력: w, h(~50)/ h개 줄에 지도 1: 땅, 0: 바다/ 마지막 줄에 0 2개
# 출력: 섬의 개수 출력
def bfs(si, sj):
    global cnt
    Q = [(si, sj)]
    visited[si][sj] = True
    while Q:
        i, j = Q.pop(0)
        for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
            ni, nj = i+di, j+dj
            if 0<=ni<h and 0<=nj<w and MAPS[ni][nj] and not visited[ni][nj]:
                Q.append((ni, nj))
                visited[ni][nj]=True
    cnt += 1

while True:
    w, h = map(int,input().split())
    if not w and not h:
        break
    MAPS = [list(map(int,input().split())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if MAPS[i][j] and not visited[i][j]:
                bfs(i, j)
    print(cnt)