# 2563
# 입력: 색종이 수/ 위치 (x, y) 10*10 정사각형
# 출력: 색종이가 붙은 영역의 넓이
N = int(input())
basic = [[0]*100 for _ in range(100)]
cnt = 0
for _ in range(N):
    R, C = map(int,input().split())
    for i in range(10):
        for j in range(10):
            if 0<=R+i <100 and 0<=C+j<100:
                basic[R+i][C+j]=1
for row in basic:
    cnt += row.count(1)
print(cnt)