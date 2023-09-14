# 4948
# 입력: 여러개의 테스트케이스, n을 포함하는 한 줄로 이루어져있다. 입력의 마지막에는 0
# 출력: n보다 크고 2n보다 작거나 같은 소수의 개수

import sys
import math

while True:
    n = int(sys.stdin.readline())
    if not n:
        break
    
    a = [False, False]+[True]*(2*n-1)
    primes=[]

    for i in range(2, 2*n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, 2*n+1, i):
                a[j] = False

    print(a[n+1:].count(True))





########## 시간초과###############
# import sys
# import math

# while True:
#     n = int(sys.stdin.readline())
#     if not n: break
#     x = n
#     cnt = 0
#     while x != 2*n+1:
#         for i in range(2, int(math.sqrt(2*n)+1)):
#             if x%i == 0:
#                 break
#         else:
#             cnt += 1
#         x+= 1
#     print(cnt)