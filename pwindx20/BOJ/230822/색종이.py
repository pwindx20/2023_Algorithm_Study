# 2563
# 입력: 색종이 수(~100)/ 색종이 위치 j, i/ 도화지 밖으로 나가는 경우는 없다, 색종이의 크기 10*10
# 출력: 색종이가 붙은 검은 영역의 넓이
N = int(input())
basic = [[0]* 100 for _ in range(100)]
cnt = 0
for _ in range(N):
    j, i = map(int, input().split())
    for k in range(10):
        for l in range(10):
            if basic[i+k][j+l] == 0:
                basic[i+k][j+l] = 1
                cnt += 1
print(cnt)