# 9063
# 입력: 점의 개수 N/ 점의 좌표 x, y
# 출력: 최소 크기의 직사각형 넓이

N = int(input())
xlst = []
ylst = []
for _ in range(N):
    x, y = map(int, input().split())
    xlst.append(x)
    ylst.append(y)
xlst.sort()
ylst.sort()
print((xlst[-1]-xlst[0])*(ylst[-1]-ylst[0]))