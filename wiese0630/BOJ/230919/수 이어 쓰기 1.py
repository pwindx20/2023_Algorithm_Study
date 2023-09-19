# N = int(input())
# ans = ''

# for num in range(1, N+1):
#     ans += str(num)

# print(len(ans))

#1트 시간초과 ㅠㅠ






# N = int(input())
# cnt = 0
# for num in range(1, N+1):
#     if 1<= num <=9:
#         cnt += 1
#     elif 10 <= num <= 99:
#         cnt += 2
#     elif 100 <= num <= 999:
#         cnt += 3
#     elif 1000 <= num <= 9999:
#         cnt += 4
#     elif 10000 <= num <= 99999:
#         cnt += 4
#     elif 100000 <= num <= 999999:
#         cnt += 5
#     elif 1000000 <= num <= 9999999:
#         cnt += 6
#     elif 10000000 <= num <= 99999999:
#         cnt += 7
#     elif 100000000 <= num <= 999999999:
#         cnt += 8
#     else:
#         cnt += 9

# print(cnt)
# 2트도 시간초과



import sys
N = int(sys.stdin.readline())
ans = 0

for num in range(1, N+1):
    ans += int(str(num))

print(ans)
#열 받아서 못하겠어요 ㅠㅠ 시간초과
