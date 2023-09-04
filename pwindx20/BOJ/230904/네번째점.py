# 3009
# 입력: 세 점의 좌표 (1~1000)
# 출력: 축과 평행한 직사각형을 만들기 위해 필요한 네번째 점
x = [0]*1001
y = [0]*1001
for _ in range(3):
    dotx, doty = map(int, input().split())
    if x[dotx]:
        x[dotx]=0
    else:
        x[dotx]=1
    if y[doty]:
        y[doty]=0
    else:
        y[doty]=1
print(x.index(1), y.index(1))