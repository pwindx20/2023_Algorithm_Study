# 11501
# 입력: T/ 날 수 N/ 날 별 주가 N개의 자연수들이 공백으로
# 출력: 최대 이익 정수
# 주식을 하나 산다/ 판다/ 아무것도 안한다
# 아... 기억안나 

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    score = list(map(int,sys.stdin.readline().split()))
    answer = 0
    sumV = 0
    cnt = 0
    while score:
        maxV = max(score)
        for i in range(len(score)):
            if score[i] == maxV:
                score = score[i+1:]
                answer += maxV*cnt - sumV
                cnt = 0
                sumV = 0
                break
            sumV += score[i]
            cnt += 1
    print(answer)


import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    score = list(map(int,sys.stdin.readline().split()))
    answer = 0
    sumV = 0
    cnt = 0
    while score:
        maxV = max(score)
        for i in range(len(score)):
            if score[i] == maxV:
                score = score[i+1:]
                answer += maxV*cnt - sumV
                cnt = 0
                sumV = 0
                break
            sumV += score[i]
            cnt += 1
    print(answer)