N,M = map(int, input().split())
arr_a = [list(map(int, input().split())) for _ in range(N)]
arr_b = [list(map(int, input().split())) for _ in range(N)]
sumV = [[0]* M for _ in range(N)]
for r in range(N):
    for c in range(M):
        sumV[r][c] = arr_a[r][c] + arr_b[r][c]
for r in range(N):
    print(*sumV[r])