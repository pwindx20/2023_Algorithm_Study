from sys import stdin
input = stdin.readline

def aaa(i, j, n):
    global cnt, save, r, c

    if n == 1:
        save = cnt
        return

    if r < i+n//2 and c < j+n//2:
        aaa(i, j, n // 2)
    elif r < i+n//2 and c >= j+n//2:
        cnt += (n//2) ** 2
        aaa(i, j + n // 2, n // 2)
    elif r >= i+n//2 and c < j+n//2:
        cnt += (n//2) ** 2 * 2
        aaa(i + n // 2, j, n // 2)
    else:
        cnt += (n // 2) ** 2 * 3
        aaa(i + n // 2, j + n // 2, n // 2)


N, r, c = map(int, input().split())
n = 2 ** N
cnt = save = 0

if r < n//2 and c < n//2:
    aaa(0, 0, n//2)
elif r < n//2 and c >= n//2:
    cnt += (n//2) ** 2
    aaa(0, n // 2, n // 2)
elif r >= n//2 and c < n//2:
    cnt += (n//2) ** 2 * 2
    aaa(n // 2, 0, n // 2)
else:
    cnt += (n//2) ** 2 * 3
    aaa(n // 2, n // 2, n // 2)

print(save)