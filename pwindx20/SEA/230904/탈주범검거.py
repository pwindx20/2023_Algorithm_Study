# 1953
# 입력: T/ 세로 N 가로 M 맨홀뚜껑 장소 세로 R 가로 C 소요시간 L/ 지하터널 지도 정보
# 출력: # t 탈주범이 위치할 수 있는 장소 개수

# 상 하 좌 우 di, dj
direction = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
# 파이프 번호 별 방향
PIPE = [[0], [1, 2, 3, 4], [1, 2], [3, 4], [1, 4], [2, 4], [2, 3], [1, 3]] 
# 방향 별 연결 가능한 파이프 번호
CONNECT = [[0], [1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7]] # 상하좌우

# 같은 거리 내의 모든 값 찾기
def bfs(sr, sc, L):
    Q = []
    visited = [[False]* M for _ in range(N)]
    Q.append((sr, sc, 1))
    visited[sr][sc] = True
    while Q:
        r, c, t = Q.pop(0)
        if t>= L:
            break
        for d in PIPE[UNDERMAP[r][c]]:
            nr, nc = r+direction[d][0], c+direction[d][1]
            if 0<= nr < N and 0<=nc<M and not visited[nr][nc]:
                if UNDERMAP[nr][nc] in CONNECT[d]:
                    Q.append((nr, nc, t+1))
                    visited[nr][nc] = True
    cnt = 0
    for row in visited:
        cnt += row.count(True)
    return cnt

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    UNDERMAP = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {bfs(R, C, L)}')