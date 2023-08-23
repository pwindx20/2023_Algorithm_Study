# 14681
# 입력: 정수 x -1000~ 1000 != 0/ 정수 y-1000~ 1000 != 0
# 출력: 사분면 번호
x = int(input())
y = int(input())
if x>0 and y>0:
    print(1)
elif x<0 and y>0:
    print(2)
elif x<0 and y<0:
    print(3)
else:
    print(4)