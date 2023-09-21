def a(n, l):
    if l == M:
        print(*str(n))
    if n % 10 < N:
        for i in range(n%10+1, N + 1):
            a(n * 10 + i, l + 1)
    else:
        return


N, M = map(int, input().split())
visited = [False] * (N+1)
for i in range(1, N+1):
    a(i, 1)