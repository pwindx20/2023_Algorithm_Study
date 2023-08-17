# 10950
# 입력: T/ A B 0 < < 10
# 출력: A+B

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(A+B)