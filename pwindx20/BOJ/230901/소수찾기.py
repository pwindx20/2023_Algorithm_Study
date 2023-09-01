# 1978
# 입력: 수의 개수 N(100이하)/N개의 수
# 출력: 소수의 개수를 출력
N = int(input())
prime = 0
for i in map(int, input().split()):
    factor = 0
    for j in range(1,i):
        if i%j == 0:
            factor += 1
    if factor == 1:
        prime += 1
print(prime)