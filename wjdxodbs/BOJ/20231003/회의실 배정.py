from sys import stdin
input = stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x:(x[1], x[0]))
cnt = 1
save = arr[0]
for i in range(1, len(arr)):
    if save[1] <= arr[i][0]:
        save = arr[i]
        cnt += 1

print(cnt)