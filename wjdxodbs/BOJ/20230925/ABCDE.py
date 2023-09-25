import sys
input = sys.stdin.readline


def ba(n, d):
    global ck
    if d == 5:
        ck = 1
        return
    visited[n] = True
    for i in arr[n]:
        if not visited[i]:
            ba(i, d+1)
            if ck:
                break
    visited[n] = False


N, M = map(int, input().split())
arr = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [False] * N
ck = 0
for i in range(N):
    if not ck:
        ba(i, 1)
    else:
        break
print(ck)