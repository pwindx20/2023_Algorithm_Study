from sys import stdin
input = stdin.readline

def a(n):
    if len(result) == M:
        print(*result)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result.append(arr[i])
            a(n + str(arr[i]))
            visited[i] = False
            result.pop()


N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
visited = [False] * N
result = []
for i in range(N):
    visited[i] = True
    result.append(arr[i])
    a(str(arr[i]))
    visited[i] = False
    result.pop()
