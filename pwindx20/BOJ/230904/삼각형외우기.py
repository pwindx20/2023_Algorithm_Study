# 10101
# 입력: 삼각형의 각 크기 3개
# 출력: 세각의 크기가 모두 60: Equilateral,
#       두 각이 같은 경우: Isosceles,
#       같은 각이 없는 경우: Scalene,
#       세 각의 합이 180이 아닌경우: Error

a=int(input()) 
b=int(input())
c=int(input())
if a+b+c != 180:
    print('Error')
else:
    if a==b==c==60:
        print('Equilateral')
    elif a==b or b==c or c==a:
        print('Isosceles')
    else:
        print('Scalene')