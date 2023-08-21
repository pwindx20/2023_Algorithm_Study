# 2491 
N = int(input())
nums = list(map(int, input().split()))
count = 1
plus_cnt = 1
minus_cnt = 1
for n in range(1, N):
    if nums[n-1] <= nums[n]:
        plus_cnt += 1
    else: 
        if count < plus_cnt:
            count = plus_cnt
        plus_cnt = 1

    if count < plus_cnt:
            count = plus_cnt    
    
    if nums[n-1] >= nums[n]:
        minus_cnt += 1
    else: 
        if count < minus_cnt:
            count = minus_cnt
        minus_cnt = 1
    
    if count < minus_cnt:
            count = minus_cnt
                
print(count)