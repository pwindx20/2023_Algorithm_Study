def dfs(r, c):
    visited = [[False] * N for _ in range(N)]
    ST = [(r, c)]
    visited[r][c] = True
    while ST:
        vr, vc = ST.pop()
        if lst[vr][vc] == '3':
            return 1
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            newR = vr + dr
            newC = vc + dc
            if 0 <= newR < N and 0 <= newC < N and lst[newR][newC] != '1':
                if not visited[newR][newC]:
                    ST.append((newR, newC))
                    visited[newR][newC] = True
    return 0


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = [list(input()) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if lst[r][c] == '2':
                print(f'#{t} {dfs(r, c)}')
                break