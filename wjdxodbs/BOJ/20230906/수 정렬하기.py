from sys import stdin
input = stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
c = [0] * 2001
for i in arr:
    c[i] += 1
lst = []
for i in range(-1000, 1001):
    if c[i]:
        lst.append(i)
print(*lst, sep='\n')