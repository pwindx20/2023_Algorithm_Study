# 2738
N, M = map(int, input().split())
A = [list(map(int,input().split())) for _ in range(N)]
B = [list(map(int,input().split())) for _ in range(N)]
for n in range(N):
    for m in range(M):
        print(A[n][m] + B[n][m], end=' ')
    print()