from collections import deque

def a(n):
    q = deque([n])
    while q:
        v = q.popleft()
        if v == M:
            return visited[v]

        for i in (v+1, v-1, v*2):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[v] + 1
                q.append(i)


N, M = map(int, input().split())
visited = [0] * 100001
print(a(N))