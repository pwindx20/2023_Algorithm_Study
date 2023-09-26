# 2667
# 입력: 지도의 크기 N/ N개의 자료 0또는 1
# 출력:  총 단지수 / 각 단지내 집의 수를 오름차순으로 정렬하여 한줄에 하나씩 출력
def bfs(si, sj):
    Q = [(si, sj)]
    visited[si][sj] = True
    cnt = 0
    while Q:
        i, j = Q.pop(0)
        cnt += 1
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and apt[ni][nj] =='1' and not visited[ni][nj]:
                visited[ni][nj] = True
                Q.append((ni, nj))
    return cnt 
                
N = int(input())
apt = [list(input()) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
result = []
for i in range(N):
    for j in range(N):
        if apt[i][j] =='1' and not visited[i][j]:
            result.append(bfs(i, j))

print(len(result))
for i in sorted(result):
    print(i)
            