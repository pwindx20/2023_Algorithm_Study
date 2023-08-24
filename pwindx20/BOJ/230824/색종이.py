# 10163
# 색종이의 변은 서로 평행하거나 수직이다.
# 입력: 색종이 장수 N(1~100)/ N장의 색종이 가장 왼쪽 아래칸의 번호 너비, 높이
#       가로, 세로 (1~1001)
# 출력: 색종이가 보이는 부분의 면적을 한 줄에 하나씩 하나의 정수로 출력
#       색종이가 보이지 않으면 정수 0 출력

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
maxr = max([x[0]+x[2] for x in paper])
maxc = max([x[1]+x[3] for x in paper])
basic = [[0]*(maxc+1) for _ in range(maxr+1)]
# basic = [[0]*1001 for _ in range(1001)]
# print(maxr, maxc)
for n in range(N):
    r, c, b, h = paper[n]
    for i in range(b):
        for j in range(h):
            # print(r, i , c, j)
            basic[r+i][c+j]= n+1
        # print(basic)
for nums in range(1,N+1):
    cnt = 0
    for p in basic:
        cnt += p.count(nums)
    print(cnt)
