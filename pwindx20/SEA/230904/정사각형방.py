# 1861
# 입력: T/ N/ N개의 정수 공백 하나로 구분되어 주어진다
# 출력: #tc 현재 방에 적힌 숫자보다 1커야만 이동할 수 있을 때 이동할 수 있는 방의 개수가 최대인 방에 적힌 수, 최대 이동 거리
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def solve():
    for i in range(N):
        for j in range(N):
            for d in range(4):
                ni, nj = i+direction[d][0], j+direction[d][1]
                if 0<=ni<N and 0<= nj<N and ROOMS[ni][nj] == ROOMS[i][j]+1:
                    COUNTS[ROOMS[i][j]] = 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ROOMS = [list(map(int, input().split())) for _ in range(N)]
    COUNTS = [0]*(N**2+1)
    solve()
    max_cnt = 0
    cnt = 0
    number = 0
    for i in range(N**2+1, 0, -1):
        if COUNTS[i] != 0:
            cnt += 1
        else:
            if max_cnt<=cnt:
                max_cnt = cnt
                number = i+1
            cnt = 0
    if max_cnt<= cnt:
        max_cnt = cnt
        number = i+1
    print(f'#{tc} {number} {max_cnt}')