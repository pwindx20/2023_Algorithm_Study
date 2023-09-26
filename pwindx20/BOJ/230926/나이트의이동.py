# 7562
# 입력: T/ 한변의 길이 I/ 나이트가 현재 있는 칸/ 이동하려는 칸
# 출력: 최소 몇번만에 이동할 수 있는지 출력
def solve(start, target):
    Q = [start]
    tx , ty = target
    while Q:
        i, j, cnt = Q.pop(0)
        if i==tx and j==ty:
            return cnt
        for di, dj in [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]:
            ni, nj = i+di, j+dj
            if 0<=ni<I and 0<=nj<I and not visited[ni][nj]:
                visited[ni][nj] = True
                Q.append((ni, nj, cnt+1))

T = int(input())
for _ in range(T):
    I = int(input())
    visited = [[False]*I for _ in range(I)]
    x, y = map(int,input().split())
    nx, ny = map(int,input().split())
    visited[x][y] = True
    print(solve((x, y, 0), (nx, ny)))