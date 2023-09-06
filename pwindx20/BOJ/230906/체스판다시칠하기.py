#1018
# 입력: N, M (8~50)/ 보드의 행 상태 B:검은색, W:흰색
# 출력: 다시 칠해야하는 정사각형 개수의 최솟값


# 하는 중
N, M = map(int, input().split())
chess = [input() for _ in range(N)]
min_cnt = 99999
for i in range(N-7):
    for j in range(N-7):
        for ver in range(2):
            cnt = 0
            row = 0
            if ver%2==0:
                while row <7:
                    if (row%2==0 and chess[i+row][j:j+8] != 'WBWBWBWB') or (row%2==1 and chess[i+row][j:j+8] != 'BWBWBWBW'):
                        cnt += chess[i+row][j:j+8].count('BB')//2
                        cnt += chess[i+row][j:j+8].count('WW')//2
                    row += 1
            else:
                while row <7:
                    if (row%2==1 and chess[i+row][j:j+8] != 'WBWBWBWB') or (row%2==0 and chess[i+row][j:j+8] != 'BWBWBWBW'):
                        cnt += chess[i+row][j:j+8].count('BB')//2
                        cnt += chess[i+row][j:j+8].count('WW')//2
                    row += 1
            if cnt <min_cnt:
                min_cnt = cnt

print(min_cnt)
                    
                    



# for i in range(N-7):
#     for j in range(M-7):
#         for k in range(8):
#             for l in range(8):
#                 for di, dj  in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
#                     ni, nj = i+di+k, j+dj+l
#                     if 0<=ni<=i+k and 0<=nj<=j+l and chess[ni][nj]==[]