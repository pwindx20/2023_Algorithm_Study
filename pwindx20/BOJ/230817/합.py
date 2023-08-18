# 8393
# 입력: n 1~10000
# 출력: 1~n까지 합

n = int(input())
total = 0
for i in range(1, n+1):
    total += i
print(total)