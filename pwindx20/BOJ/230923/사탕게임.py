# 3085
# 입력: N/사탕 색상 C, P, Z, Y
# 출력: 먹을 수 있는 사탕의 최대 개수
def solve(pos1, pos2):
    global max_candy
    x, y = pos1
    nx, ny = pos2
    c1 = arr[x][y]
    c2 = arr[nx][ny]
    c1_cnt = 0
    c2_cnt = 0
    for i in range(N):
        # 행고정
        if arr[x][i] ==c1:
            c1_cnt += 1
        else:
            if max_candy<c1_cnt:
                max_candy = c1_cnt
            c1_cnt = 0
        
    # 초기화
    if max_candy<c1_cnt:
        max_candy = c1_cnt
    c1_cnt = 0

    for i in range(N):
        # 열고정
        if arr[i][y] ==c1:
            c1_cnt +=1
        else:
            if max_candy<c1_cnt:
                max_candy = c1_cnt
            c1_cnt = 0
    # 초기화
    if max_candy<c1_cnt:
        max_candy = c1_cnt
    c1_cnt = 0

    for i in range(N):
        # 행고정
        if arr[nx][i] ==c2:
            c2_cnt += 1
        else:
            if max_candy<c2_cnt:
                max_candy = c2_cnt
            c2_cnt = 0
        
    # 초기화
    if max_candy<c2_cnt:
        max_candy = c2_cnt
    c2_cnt = 0

    for i in range(N):
        # 열고정
        if arr[i][y] ==c2:
            c2_cnt +=1
        else:
            if max_candy<c2_cnt:
                max_candy = c2_cnt
            c2_cnt = 0
    # 초기화
    if max_candy<c2_cnt:
        max_candy = c2_cnt
    c2_cnt = 0
        
N = int(input())
arr = [list(input()) for _ in range(N)]
max_candy = 0
for i in range(N):
    for j in range(N):
        for di, dj in [(1, 0), (0, 1)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N:
                arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j]
                solve((i, j), (ni, nj))
                arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j]

print(max_candy)