#10157
# C, R (x, y) 1부터 시작
# 입력: 5<=C, R <1000 , 대기번호 1~100,000,000
# 출력: K번인 관객에게 배정될 좌석번호 x,y를 출력, 배정할 수 없는 경우 0

C, R = map(int, input().split())
K = int(input())
if K > C*R:
    print(0)
else:
    basic = [[0]*(C+1) for _ in range(R+1)]
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    r, c = 1, 1
    d = 0
    for value in range(1,K):
        basic[r][c] = value
        nr = r+dr[d]
        nc = c+dc[d]
        if not(0< nr <= R) or not(0< nc <= C) or basic[nr][nc] != 0:
            d = (d+1)%4
            nr = r+dr[d]
            nc = c+dc[d]
        r = nr
        c = nc
    # print(basic)
    print(c, r)
   