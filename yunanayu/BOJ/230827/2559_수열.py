import sys
input = sys.stdin.readline
#
# N, K = map(int, input().split())    # N = 온도 측정 날짜의 수 K = 합을 구하기 위한 연속 날짜
# Temp = list(map(int, input().split()))
# # print(Temp)
# # max_t = 0
# # for i in range(N-K+1):
# #     ans = 0
# #     for j in range(K):
# #         ans += Temp[i+j]
# #     if max_t < ans:
# #         max_t = ans
# # print(max_t)
#
# # lst = []
# # for i in range(N-K+1):
# #     ans = 0
# #     for j in range(K):
# #         ans += Temp[i+j]
# #     lst.append(ans)
# # print(max(lst))
# #
# # lst = []
# # for i in range(N-K+1):
# #     ans = sum(Temp[i:i+K])
# #     lst.append(ans)
# # print(max(lst))
#
# lst = []
# for i in range(N-K+1):
#     lst.append(sum(Temp[i:i+K]))
# print(max(lst))

N, K = map(int, input().split())
lst = list(map(int, input().split()))
S_lst = [0]
for l in lst:
    S_lst.append(S_lst[-1]+l)
# print(S_lst)  # [0, 3, 1, -3, -12, -12, -9, -2, 11, 19, 16]
result = -2147483648
for i in range(N-K+1):
    S = S_lst[K+i] - S_lst[i]
    if result < S:
        result = S
print(result)