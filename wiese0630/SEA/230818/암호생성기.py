T = 10

for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    # print(nums)

    minusV = 1
    while nums[-1] > 0:
        v = nums.pop(0)
        nums.append(v-minusV)
        if nums[-1] < 0:
            nums[-1] = 0
        minusV += 1

        if minusV == 6:
            minusV = 1
    # print(nums)

    ans = ' '.join(map(str, nums))
    print(f'#{test_case} {ans}')