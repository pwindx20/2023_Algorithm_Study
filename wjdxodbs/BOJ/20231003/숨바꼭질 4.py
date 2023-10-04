from collections import deque

def aaa(n):
    q = deque()
    q.append(n)
    visited[n][0] = 0

    while q:
        v = q.popleft()
        if v == K:
            save = [v]
            item = visited[v][1]
            while item != -1:
                save.append(item)
                item = visited[item][1]
            return [visited[v][0], save]

        for i in (v+1, v-1, v*2):
            if 0 <= i <= 100000 and visited[i][0] == -1:
                q.append(i)
                visited[i][0] = visited[v][0] + 1
                visited[i][1] = v

N, K = map(int, input().split())
visited = [[-1, -1] for _ in range(100001)]
n, lst = aaa(N)
print(n)
print(*reversed(lst))
