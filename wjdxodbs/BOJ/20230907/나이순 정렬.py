from sys import stdin
input = stdin.readline

N = int(input())
arr = [[] for _ in range(100001)]
for _ in range(N):
    a, b = input().split()
    arr[int(a)].append(b)
for i in range(1, 100001):
    for j in arr[i]:
        print(i, j)