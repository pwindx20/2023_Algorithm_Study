def a(n, l):
    if l == M:
        print(*str(n))
        return
    if n % 10 <= N:
        for i in range(n % 10, N + 1):
            a(n * 10 + i, l + 1)
    else:
        return


N, M = map(int, input().split())
for i in range(1, N+1):
    a(i, 1)