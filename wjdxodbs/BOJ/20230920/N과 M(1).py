def a(n, l):
    if l == M:
        print(*str(n))
    for i in range(1, N + 1):
        if visited[i] == False:
            visited[i] = True
            a(n*10+i, l+1)
            visited[i] = False


N, M = map(int, input().split())
visited = [False] * (N+1)
for i in range(1, N+1):
    visited[i] = True
    a(i, 1)
    visited[i] = False