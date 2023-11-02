# 2512
# 입력: 지방의 수 N/ 지방의 예산 요청 N개의 정수/ 총 예산 M
# 출력: 배정된 예산 중 최댓값
# 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
# 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다.
# 상한 액 이하의 예산 요청에 대해서는 요청한 금액을 그대로 배정한다.

N = int(input())
budgets = list(map(int,input().split()))
M = int(input())













################
# 10
# 1 1 1 1 11 11 11 11 11 100
# 100
# 16
# 정답은 41
#########################
# N = int(input())
# budgets = list(map(int,input().split()))
# M = int(input())

# avg = M//N
# remain = 0
# remain2 = 0
# cnt = N
# for budget in budgets:
#     if budget <= avg:
#         cnt-=1
#         remain2 += avg-budget
#     remain += avg-budget
# if remain>0:
#     print(max(budgets))
# else:
#     print((remain2+avg*cnt)//cnt)