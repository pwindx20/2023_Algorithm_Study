arr = [[0]*1001 for _ in range(1001)]
N = int(input())
cnt = 1
for _ in range(N):
    c, r, w, h = map(int, input().split())
    for i in range(r,r+h):
        for j in range(c,c+w):
            arr[i][j] = cnt
    cnt += 1

for i in range(1, N+1):
    ans = 0
    for r in range(1001):
        for c in range(1001):
            if arr[r][c] == i:
                ans += 1
    print(ans)
    
