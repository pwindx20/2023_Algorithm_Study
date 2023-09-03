N = int(input())
nums = list(map(int, input().split()))
cnt = 0
for num in nums:
    if num != 1:
        no = 0
        for i in range(2,num):
            if num % i == 0:
                no += 1
        if no == 0:
            cnt += 1
print(cnt)