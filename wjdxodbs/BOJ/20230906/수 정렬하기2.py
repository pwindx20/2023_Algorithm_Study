from sys import stdin
input = stdin.readline

N = int(input())
lst = [0] * 2000001
for i in range(N):
    lst[int(input())] += 1
for i in range(-1000000, 1000001):
    if lst[i]:
        print(i)