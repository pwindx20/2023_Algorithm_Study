def a(idx, n):
    if len(n) == N:
        print(*n)
        return

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            a(idx + 1, n + str(i))
            visited[i] = False


N = int(input())
visited = [False] * (N+1)
a(1, '')