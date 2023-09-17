# 2753
# 입력: 연도(1~4000)
# 출력: 윤년 1, 아닐시 0
y = int(input())
if y%4 == 0:
    if y%100 !=0 or y%400 == 0:
        print(1)
    else:
        print(0)
else: print(0)