# 1189
# 입력: R(1~5), C(1~5), 거리 K(1~R*C) / 맵의 정보 T 는 갈 수 없는 곳
# 출력: 거리가 K인 가짓수
def solution(i, j, d):
    global count
    if d==K and i==0 and j==C-1:
        count += 1
        return

    if (i==0 and j==C-1) or d>=K:
        return
    
    for di, dj  in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i+di, j+dj
        if 0<=ni<R and 0<=nj<C and not visited[ni][nj]:
            visited[ni][nj] = 1
            solution(ni, nj, d+1)        
            visited[ni][nj] = 0
            
            
R, C, K = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'T':
            visited[i][j] = 1
# 초기 출발 부분 visited
visited[R-1][0] = 1
count = 0
solution(R-1,0,1)
print(count)


# def bfs(si, sj, K):
#     global count
#     Q = []
#     Q.append((si, sj, 1))
#     visited[si][sj] = 1
#     while Q:
#         i, j, d = Q.pop(0)
#         if d==K and i==0 and j==C-1:
#             count += 1   
#         for di, dj  in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#             ni, nj = i+di, j+dj
#             if 0<=ni<R and 0<=nj<C and not visited[ni][nj]:
#                 visited[ni][nj] = 1
#                 Q.append((ni, nj, d+1))