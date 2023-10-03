from collections import deque
import sys
input = sys.stdin.readline

def BFS(n):
    q = deque()
    q.append(n)
    while q:
        v = q.popleft()
        for i in arr[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                lst[i] = v


N = int(input())
arr = [[] for _ in range(N+1)]
lst = [0] * (N+1)
visited = [False] * (N+1)
visited[1] = True
for i in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
BFS(1)
print(*lst[2:], sep='\n')