# 4615
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    basic = [[0]*(N) for _ in range(N)]
    basic[N//2][N//2] = basic[N//2-1][N//2-1] = 2
    basic[N//2-1][N//2] = basic[N//2][N//2-1] = 1
    for _ in range(M):
        i, j, s = map(int, input().split())
        i = i-1
        j = j-1
        basic[i][j] = s
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
            k = 1
            ch_lst = []
            while k<N: 
                ni = i+k*di
                nj = j+k*dj
                if 0<= ni <N and 0<= nj<N:
                    if basic[ni][nj]==0:
                        break
                    elif basic[ni][nj]== (s%2)+1:
                        k+=1
                        ch_lst.append((ni, nj))
                        continue
                    else:
                        for nni, nnj in ch_lst:
                            basic[nni][nnj] = s
                break
        
        b_cnt = w_cnt = 0
        for row in basic:
            b_cnt += row.count(1)
            w_cnt += row.count(2)
    print(f'#{tc} {b_cnt} {w_cnt}')