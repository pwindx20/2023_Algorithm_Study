# 수열

N = int(input())
lst = list(map(int, input().split()))

max1 = 0
max2 = 0
increase = 1
decrease = 1

for l in range(0, N-1):
    if lst[l] <= lst[l+1]:
        increase += 1
        if increase > max1:
            max1 = increase
    else:
        increase = 1

for i in range(0, N-1):
    if lst[i] >= lst[i+1]:
        decrease += 1
        if decrease > max2:
            max2 = decrease
    else:
        decrease = 1
print(max(max1, max2))