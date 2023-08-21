# 15552
# 입력: T ~1000000/ A, B 1~1000
# 출력: A+B
import sys
T = int(input())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split()) # sys.stdin.readline()은 한줄 단위로 입력받기 때문에, 개행문자가 같이 입력 받아집니다.
    print(A+B)


# T = int(input())
# for _ in range(T):
#     A, B = map(int, input().split())
#     print(A+B)