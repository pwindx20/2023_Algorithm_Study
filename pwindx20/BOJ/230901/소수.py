# 2581
# 입력: M/ N 
# 출력: M~N 중 소수를 골라 소수의 합/ 최솟값을 출력 (소수가 없을 경우 -1 출력)

M = int(input())
N = int(input())
primes = []
for i in range(M, N+1):
    factor = 0
    for j in range(1,i):
        if i%j == 0:
            factor+= 1
    if factor == 1:
        primes.append(i)
if primes:
    print(sum(primes))
    print(primes[0])
else:
    print(-1)