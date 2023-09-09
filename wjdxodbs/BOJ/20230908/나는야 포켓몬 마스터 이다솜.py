from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]
d = {arr[i]: i+1 for i in range(N)}
for i in range(M):
    a = input().rstrip()
    print(arr[int(a)-1] if a.isdigit() else d[a])