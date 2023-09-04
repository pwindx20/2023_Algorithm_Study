# 14215
# 입력: a, b, c
# 출력: 만들 수 있는 삼각형 중 가장 큰 둘레의 길이

lst = list(map(int, input().split()))
lst.sort()
a, b, c = lst
if c>= a+b:
    print(2*(a+b)-1)
else:
    print(a+b+c)