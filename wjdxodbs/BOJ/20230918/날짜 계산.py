def a(idx, N):
    global save, ck
    n = 0
    while arr[idx] * n + lst[idx] < N:
        n += 1
    if arr[idx] * n + lst[idx] == N:
        if idx < 2:
            a(idx + 1, arr[idx] * n + lst[idx])
        elif idx == 2:
            ck = 1
            save = arr[idx] * n + lst[idx]


lst = list(map(int, input().split()))
arr = [15, 28, 19]
idx = n = ck = save = 0
while not ck:
    a(idx + 1, arr[idx] * n + lst[idx])
    n += 1
print(save)