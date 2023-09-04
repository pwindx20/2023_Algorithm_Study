M = int(input())
N = int(input())
lst = []
for num in range(M, N+1):
    if num != 1:    # 1 꼭 제외시키기 잊지말기 무조건무조건 잊지말자
        no = 0
        for n in range(2,num):
            if num % n == 0:
                no = 1
                break
        if no == 0:
            lst.append(num)
if lst:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)