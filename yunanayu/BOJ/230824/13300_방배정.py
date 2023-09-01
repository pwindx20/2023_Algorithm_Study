N, K = map(int, input().split())
arr = [[0,0] for _ in range(6)]
cnt = 0
for _  in range(N):
    S, Y = map(int, input().split())
    arr[Y-1][S] += 1
for i in arr:
    for j in range(2):
        if i[j] % K == 0:
            cnt += i[j]//K
        elif i[j] != 0:
            cnt = cnt + i[j]//K + 1
        else:
            continue
print(cnt)