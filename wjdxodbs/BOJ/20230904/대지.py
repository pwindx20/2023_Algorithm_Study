from sys import stdin
input = stdin.readline

N = int(input())
r = []
c = []
for i in range(N):
    a, b = map(int, input().split())
    r.append(a)
    c.append(b)
result = (max(r) - min(r)) * (max(c) - min(c))
print(result)