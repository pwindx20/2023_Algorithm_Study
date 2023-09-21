def a(n, l):
    if l == M:
        print(*str(n))
        return
    for i in range(1, N + 1):
        a(n * 10 + i, l + 1)


N, M = map(int, input().split())
for i in range(1, N+1):
    a(i, 1)