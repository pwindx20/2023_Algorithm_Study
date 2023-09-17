def f(k, curS):
    global resultMin
    if curS > resultMin:
        return

    if k==N:
        # #print(result)
        # sumV = 0
        # for kt in range(N):
        #     c = result[kt]
        #     sumV += arr[kt][c]
        if curS < resultMin:
            resultMin = curS
        return

    for i in range(N):
        if not used[i]:
            used[i] = True
            result[k] = i
            f(k+1, curS+arr[k][i])
            used[i] = False

    return


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    result = [-1] * N
    used = [False] * N
    resultMin = 10*10*10
    f(0, 0)
    print(f'#{test_case} {resultMin}')

