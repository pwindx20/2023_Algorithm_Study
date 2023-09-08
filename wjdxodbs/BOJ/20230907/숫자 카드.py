from sys import stdin
input = stdin.readline

N = int(input())
arr = set(map(int, input().split()))
M = int(input())
lst = list(map(int, input().split()))
for i in lst:
    if i in arr:
        print(1, end=' ')
    else:
        print(0, end=' ')