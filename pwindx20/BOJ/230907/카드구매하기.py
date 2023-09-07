# 11052
# 입력: 구매하려고 하는 카드의 개수 N/ Pi
# 출력: N개의 카드를 갖기 위해 지불해야하는 금액의 최댓값

# 오... 모르겠음

# ### 다른사람코드###
# dp[i] = 카드 i개를 구매하는 최대 가격, p[k] = k개가 들어있는 카드팩 가격
# > dp[i] = p[i] +dp[i-k]
# 1부터 k개까지 차례대로 식을 써보면서 점화식을 만드는게 중요한 것 같다.

N = int(input())
p=[0]+list(map(int, input().split()))
dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j]+p[j])
print(dp[i])


########잘못접근함#########################
# def partial(k, sumN, sumV):
#     global maxV
#     if sumN >N:
#         return
    
#     if k==N:
#         print(bits)
#         if sumN == N and maxV<sumV:
#             maxV = sumV
#         return

#     bits[k]=0
#     partial(k+1, sumN, sumV)
#     bits[k]=1
#     partial(k+1, sumN+k, sumV+Pi[k])


# N = int(input())
# Pi = [0]+list(map(int,input().split()))
# bits = [0]*(N+1)
# maxV = 0
# partial(0,0,0)
# print(maxV)