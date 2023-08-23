T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    # print(nums)

    for i in range(M):
        v = nums.pop(0)
        nums.append(v)
    ans = nums[0]

    print(f'#{test_case} {ans}')