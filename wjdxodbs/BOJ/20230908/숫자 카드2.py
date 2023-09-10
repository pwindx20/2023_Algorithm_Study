from sys import stdin
input = stdin.readline

N = int(input())
arr1 = list(input().split())
M = int(input())
arr2 = list(input().split())
d = {}
for i in arr1:
    d.setdefault(i, 0)
    d[i] += 1
for i in arr2:
    print(d.get(i, 0), end=' ')