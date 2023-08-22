arr = [[0] * 100 for _ in range(100)]
N = int(input())
for _ in range(N):
    P1, P2 = map(int,input().split()) # 색종이 왼쪽변과 도화지 왼쪽 변 사이의 거리/ 색종이 아랫변과 도화지 아랫변 사이의 거리
    for r in range(P1, P1+10):
        for c in range(P2, P2+10):
            arr[r][c] = 1

cnt = 0
for i in range(100):
    for j in range(100):
       if arr[i][j] == 1:
           cnt += 1

print(cnt)