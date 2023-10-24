from sys import stdin
input = stdin.readline

def a(idx, n):
    global max_n
    if idx >= N:
        if max_n < n:
            max_n = n
        return

    a(idx + 1, n)
    if idx + arr[idx][0] > N:
        a(idx + arr[idx][0], n)
    else:
        a(idx + arr[idx][0], n + arr[idx][1])


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_n = 0
for i in range(N):
    if i + arr[i][0] <= N:
        a(i + arr[i][0], arr[i][1])
print(max_n)
