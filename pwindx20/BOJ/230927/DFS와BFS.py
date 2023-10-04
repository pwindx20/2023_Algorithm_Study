# 1260
# 입력: 정점의 개수 N(~1000), 간선의 개수 M(~10000) 탐색을 시작할 번호 V/ 두 정점의 번호 양방향
# 출력: DFS 수행결과 BFS 수행결과
import sys
from collections import deque

def dfs(start):
    

# def bfs(start):
#     visited = [True]+[False]*N
#     Q = deque()
#     Q.append(start)
#     visited[start] = True
#     while Q:
#         v = Q.popleft()
#         print(v, end=' ')
#         for w in G[v]:
#             if not visited[w]:
#                 Q.append(w)
#                 visited[w] = True
        
# def dfs(start):
#     visited = [True]+[False]*N
#     ST = deque()
#     ST.append(start)
#     visited[start] = True
#     while ST:
#         v = ST.pop()
#         print(v, end=' ')
#         for w in G[v]:
#             if not visited[w]:
#                 ST.append(w)
#                 visited[w] = True
                

N, M, V = map(int,input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int,sys.stdin.readline().split())
    G[v1].append(v2)
    G[v2].append(v1)

dfs(V)
print()
bfs(V)