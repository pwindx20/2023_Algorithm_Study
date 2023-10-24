from sys import stdin
input = stdin.readline

N, S, R = map(int, input().split())
m = list(map(int, input().split()))
p = list(map(int, input().split()))
arr = [0] * N

for i in m:
    arr[i-1] -= 1
for i in p:
    arr[i-1] += 1

for i in range(N):
    if arr[i] == 1:
        if i == 0:
            if arr[i + 1] == -1:
                arr[i + 1] = 0
                arr[i] = 0
        elif i == N-1:
            if arr[i - 1] == -1:
                arr[i - 1] = 0
                arr[i] = 0
        else:
            if arr[i - 1] == -1:
                arr[i - 1] = 0
                arr[i] = 0
            elif arr[i + 1] == -1:
                arr[i + 1] = 0
                arr[i] = 0


print(arr.count(-1))