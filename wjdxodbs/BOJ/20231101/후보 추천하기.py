from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())
arr = list(map(int, input().split()))
save = [[0, 0]] * N
for i in range(M):
    lst = [item for item in save if item[0] == arr[i]]
    if lst:
        save[save.index(lst[0])][1] += 1
    else:
        if save.count([0, 0]):
            save[save.index([0, 0])] = [arr[i], 1]
        else:
            min_n = [0, int(1e9)]
            cnt = 0
            for j in range(N):
                if min_n[1] > save[j][1]:
                    min_n = save[j]
                    cnt = 1
                elif min_n == save[j][1]:
                    cnt += 1

            if cnt:
                idx = save.index(min_n)
                save[idx] = [arr[i], 1]
                for j in range(idx+1, N):
                    save[j-1], save[j] = save[j], save[j-1]
result = sorted([i[0] for i in save if i[1] != 0])
print(*result)