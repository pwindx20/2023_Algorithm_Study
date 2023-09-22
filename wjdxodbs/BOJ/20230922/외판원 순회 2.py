from sys import stdin
input = stdin.readline


def a(idx, c, cost, start):
    global min_n
    if c == N:
        min_n = min(cost, min_n)
        return

    for item in graph[idx]:
        if c == N-1 and item[0] == start:
            a(item[0], c + 1, cost + item[1], start)
        elif not visited[item[0]]:
            if min_n > cost+item[1]:
                visited[item[0]] = True
                a(item[0], c + 1, cost + item[1], start)
                visited[item[0]] = False


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
graph = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            graph[i].append((j, arr[i][j]))
visited = [False] * N
min_n = int(1e10)

for i in range(N):
    visited[i] = True
    a(i, 0, 0, i)
    visited[i] = False
print(min_n)