# 1735
# 입력: 분수의 분자, 분모 2줄
# 출력: 기약분수의 분자와 분모

A1, A2 = map(int,input().split())
B1, B2 = map(int,input().split())

C1, C2 = A1*B2+B1*A2, A2*B2
c1, c2 = C1, C2
while c2>0:
    c1, c2 = c2, c1%c2
print(C1//c1, C2//c1)
