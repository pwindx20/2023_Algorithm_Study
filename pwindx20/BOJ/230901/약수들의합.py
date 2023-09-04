# 9506
# 입력: n(2~100,000)/ 마지막엔 -1
# 출력: n이 완전수(자신을 제외한 모든 약수들의 합과 같음): n을 제외한 약수들의 합
#       n = f1 + f2 + f3 ...
#       아닐시 n in NOT perfect.

while True:
    n = int(input())
    if n == -1:
        break
    factor = []
    for i in range(1, n):
        if n % i == 0:
            factor.append(i)
    if sum(factor) == n:
        print(f'{n} = {" + ".join(map(str,factor))}')
    else:
        print(f'{n} is NOT perfect.')