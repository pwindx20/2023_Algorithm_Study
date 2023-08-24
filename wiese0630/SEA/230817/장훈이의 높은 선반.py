T = int(input())

for test_case in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    # print(N, B, arr)

    n = len(arr)

    min = 10000
    for i in range(1 << n):
        sumV = 0
        for j in range(n):
            if i & (1 << j):
                sumV += arr[j]


        if sumV >= B:
            result = sumV - B
            if result < min:
                min = result
    ans = min


    print(f'#{test_case} {min}')