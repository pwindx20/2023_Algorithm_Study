from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
ck = 0
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            n = arr[i]+arr[j]+arr[k]
            if ck < n <= M:
                ck = n
print(ck)