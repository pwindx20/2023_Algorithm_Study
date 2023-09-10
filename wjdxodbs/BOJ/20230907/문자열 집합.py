from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
S = set(input().rstrip() for _ in range(N))
cnt = 0
for i in range(M):
    if input().rstrip() in S:
        cnt += 1
print(cnt)