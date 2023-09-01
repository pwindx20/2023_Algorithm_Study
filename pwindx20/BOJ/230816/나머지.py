# 10430
# 입력: A, B, C 2~10000
# 출력: (A+B)%C/ ((A%C)+(B%C))/ (A*B)%C/ ((A%C)*(B%C))%C
A, B, C = map(int, input().split())
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)