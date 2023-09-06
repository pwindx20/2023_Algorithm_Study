from sys import stdin
input = stdin.readline

N = int(input())
lst = [0] * 10001
for i in range(N):
    lst[int(input())] += 1
for i in range(1, 10001):
    for j in range(lst[i]):
        print(i)