from sys import stdin
input = stdin.readline

N = int(input())
arr = [[] for _ in range(200001)]
for _ in range(N):
    a, b = map(int, input().split())
    arr[a].append(b)
for i in range(200001):
    arr[i] = sorted(arr[i])
for i in range(-100000, 100001):
    if arr[i]:
        for j in arr[i]:
            print(i, j)