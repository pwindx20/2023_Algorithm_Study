def change(sr,sc):
    for i in range(sr, sr+3):
        for j in range(sc, sc+3):
            if A[i][j] == '0':
                A[i][j] = '1'
            else:
                A[i][j] = '0'


def check(A, B):
    for r in range(N):
        for c in range(M):
            if A[r][c] != B[r][c]:
                return False
    return True



N, M = map(int, input().split())
A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(N)]
# print(A)
# print(B)
ans = 0
if N < 3 and M < 3:
    if check(A, B):
        print(0)
    else:
        print(-1)
else:
    for r in range(N-2):
        for c in range(M-2):
            if A[r][c] != B[r][c]:
                change(r,c)
                ans += 1

    if check(A, B):
        print(ans)
    else:
        print(-1)