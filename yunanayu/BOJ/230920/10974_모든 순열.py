def per(k):
    if k == N:
        for i in range(N):
            position = result[i]
            print(lst[position],end=' ')
        print()
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result[k] = i
            per(k+1)
            visited[i] = False

N = int(input())
lst = [i for i in range(1, N+1)]
result = [-1] * N
visited = [False] * N
per(0)