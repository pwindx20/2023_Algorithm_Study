from sys import stdin
input = stdin.readline

s = set()
N = int(input())
for i in range(N):
    a = list(input().split())
    if a[0] in s:
        s.remove(a[0])
    else:
        s.add(a[0])
print(*sorted(s, reverse=True), sep='\n')