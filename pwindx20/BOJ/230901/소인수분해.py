# 11653
# 입력: 정수 N
# 출력: N의 소인수분해 결과를 한줄에 하나씩 오름차순으로 출력
#       N이 1인 경우 아무것도 출력하지 않는다.

N = int(input())
i = 2
while N != 1:
    if N % i == 0:
        N //= i
        print(i)
    else:
        i += 1

        