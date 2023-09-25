# 13023
# 입력: 사람 수 N(5~2000) 친구관계 수 M(1~2000)/ a, b
# 출력: A, B, C, D, E가 존재하면 1, 없으면 0
# A, B는 친구 B, C는 친구, C, D는 친구, D, E는 친구 인 경우가 있는지 없는지
from collections import deque
def solve(start, depth):
    global isF
    if depth >=5:
        isF = 1
        return
    for v in G[start]:
        if not visited[v]:
            visited[v] = True
            solve(v, depth+1)
            visited[v] = False
    
    
N, M = map(int,input().split())
G = [[] for _ in range(N)]
visited = [False]*N
for _ in range(M):
    x, y = map(int,input().split())
    G[x].append(y)
    G[y].append(x)
isF = 0
i = 0
while not isF and i<N:
    visited[i] = True
    solve(i, 1)
    visited[i] = False
    i+= 1

print(isF)