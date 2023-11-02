from sys import stdin
input = stdin.readline

def bfs(a):
    q = [a]
    visited = [-1] * (n+1)
    visited[a] = 0
    while q:
        v = q.pop(0)
        if v == b:
            return visited[v]
        for i in arr_b[v]:
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[v] + 1
    return -1


n = int(input())
a, b = map(int, input().split())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(m)]
arr_b = [[] for _ in range(n+1)]
for i in arr:
    arr_b[i[0]].append(i[1])
    arr_b[i[1]].append(i[0])
print(bfs(a))