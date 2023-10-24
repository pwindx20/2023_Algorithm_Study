from sys import stdin
input = stdin.readline

def bfs(i):
    q = [i]
    visited[i] = True
    while q:
        v = q.pop(0)
        for item in arr[v]:
            if visited[item] == False:
                q.append(item)
                visited[item] = True


N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
cnt = 0
visited = [False] * (N+1)
for i in range(1, len(arr)):
    if arr[i] and visited[i] == False:
        bfs(i)
        cnt += 1
cnt += (visited.count(False)-1)
print(cnt)