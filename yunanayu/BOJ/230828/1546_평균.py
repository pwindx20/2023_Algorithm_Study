# 평균
N = int(input())
lst = list(map(int, input().split()))
M = max(lst)
for i in range(N):
    lst[i] = lst[i]/M*100
avg = sum(lst)/N
print(avg)