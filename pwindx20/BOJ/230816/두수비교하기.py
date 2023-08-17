# 1330
# 입력: A, B
# 출력: > < ==
A, B = map(int, input().split())
if A>B:
    print('>')
elif A<B:
    print('<')
else:
    print('==')