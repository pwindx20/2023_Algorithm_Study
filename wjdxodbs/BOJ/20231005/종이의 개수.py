from sys import stdin
input = stdin.readline

def aaa(r, c, n):
    save = arr[r][c]
    b = 0

    for i in range(r, r+n):
        for j in range(c, c+n):
            if save != arr[i][j]:
                for a in range(r, r+n, n//3):
                    aaa(a, c, n//3)
                    aaa(a, c+n//3, n//3)
                    aaa(a, c+2*n//3, n//3)
                b = 1
                break
        if b:
            break
    else:
        lst[save] += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
lst = [0] * 3
save = arr[0][0]
b = 0

for i in range(N):
    for j in range(N):
        if save != arr[i][j]:
            for a in range(0, N, N//3):
                aaa(a, 0, N//3)
                aaa(a, N//3, N//3)
                aaa(a, 2*N//3, N//3)
            b = 1
            break
    if b:
        break
else:
    lst[save] += 1

for i in range(-1, 2):
    print(lst[i])