import sys
input = sys.stdin.readline

K = int(input())
ST = []
for _ in range(K):
    n = int(input())
    if n != 0:
        ST.append(n)
    else:
        ST.pop()
print(sum(ST))
