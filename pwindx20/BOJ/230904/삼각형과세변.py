# 5073
# 입력: 양의 정수 3개 마지막줄은 0 0 0
# 출력: 세변의 길이가 모두 같은 경우: Equilateral
#       두 변의 길이만 같은 경우: Isosceles
#       세 변의 길이가 모두 다른 경우: Scalene
#       긴 변의 길이보다 나머지 두변의 길이의 합이 길지 않으면: Invalid

while True:
    lst = sorted(list(map(int,input().split())))
    a, b, c = lst
    if a==b==c== 0:
        break
    if c>= a+b:
        print('Invalid')
    else:
        if a==b==c:
            print('Equilateral')
        elif a==b or b==c or c==a:
            print('Isosceles')
        else:
            print('Scalene')
    
    