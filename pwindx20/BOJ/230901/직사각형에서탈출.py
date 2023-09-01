# 1085
# 입력: x, y, w, h
# 출력: 직사각형의 경계선까지 가는 거리의 최솟값을 구하시오
x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))