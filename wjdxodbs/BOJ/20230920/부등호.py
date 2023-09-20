def a(n, c):
    if c == N:
        result.append(n)
        return

    if arr[c] == '<':
        for i in range(int(n[-1])+1, 10):
            if not visited[i]:
                visited[i] = True
                a(n + str(i), c + 1)
                visited[i] = False
    else:
        for i in range(int(n[-1])-1, -1, -1):
            if not visited[i]:
                visited[i] = True
                a(n+str(i), c+1)
                visited[i] = False


N = int(input())
arr = list(input().split())
result = []
visited = [False] * 10
for i in range(10):
    visited[i] = True
    a(str(i), 0)
    visited[i] = False
save = result[0]
result = [int(i) for i in result]
print(f'{max(result)}\n{save}')