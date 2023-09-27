from sys import stdin
input = stdin.readline

def dfs(V):
    st = [V]
    visited = [False] * (N+1)
    while st:
        v = st.pop()
        if not visited[v]:
            visited[v] = True
            print(v, end=' ')

        for i in node1[v]:
            if not visited[i]:
                st.append(i)

def bfs(V):
    q = [V]
    visited = [False] * (N+1)
    while q:
        v = q.pop(0)
        if not visited[v]:
            visited[v] = True
            print(v, end=' ')
        for i in node[v]:
            if not visited[i]:
                q.append(i)


N, M, V = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
node = [[] for _ in range(N+1)]
for i, j in arr:
    node[i].append(j)
    node[j].append(i)
node = [sorted(i) for i in node]
node1 = [sorted(i, reverse=True) for i in node]
dfs(V)
print()
bfs(V)