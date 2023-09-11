# 1934
# 입력: T/ A, B
# 출력: A와 B의 최소공배수
import sys
T= int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    if A>B:
        x, y = B, A
    else: x, y = A, B
        
    # 유클리드 호제법
    while y:
        x, y = y, x % y

    print(A*B//x)

#########시간 초과###############
# import sys
# T= int(sys.stdin.readline())
# for _ in range(T):
#     A, B = map(int, sys.stdin.readline().split())
#     if A>B:
#         A, B = B, A
#     i = A
#     m = 1
#     while i!=1 and A!=1:
#         # print(A, B, i)
#         if B%i==0 and A%i==0:
#             B//=i
#             A//=i
#             m*=i
#             i= A+1
#         i-=1
    
#     print(A*B*m)