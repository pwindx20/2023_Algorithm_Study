# 4615
# 입력: T/ 한변의 길이 N(4,6,8) , 돌을 놓는 횟수 M/ 돌의 위치, 돌의 색(1:흑, 2: 백)
# 출력: # tc 흑돌, 백돌 갯수
# 가운데에 돌을 놓고 시작, 자신이 놓은 돌과 자신의 돌 사이에 상태편의 돌이 있을 경우에만 가능

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    basic = [[0]* N for _ in range(N)]
    basic[N//2][N//2] = basic[N//2-1][N//2-1] = 2
    basic[N//2-1][N//2] = basic[N//2][N//2-1] = 1
    
    for _ in range(M):
        i, j, order = map(int, input().split())
        i=i-1
        j = j-1
        basic[i][j] = order
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
            for k in range(1,N):
                ni, nj = i+k*di, j+k*dj
                if 0 <= ni < N and 0<=nj<N:
                    if basic[ni][nj] == order%2+1:
                        continue
                    else:
                        if basic[ni][nj] == order:
                            for a in range(1, k):
                                basic[i+a*di][j+a*dj] = order
                        break
                        
        # print(basic)
    b_cnt = 0
    w_cnt = 0
    for arr in basic:
        b_cnt += arr.count(1)
        w_cnt += arr.count(2)
    
    print(f'#{tc} {b_cnt} {w_cnt}')