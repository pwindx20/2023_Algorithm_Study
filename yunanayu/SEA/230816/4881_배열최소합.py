def f(k, curM):
    global resultMin

    if curM > resultMin:
        return

    if k == N:
        if curM < resultMin:
            resultMin = curM

        return

    for i in range(N):
        if not used[i]:  # 위에서 사용 안한경우
            used[i] = True
            result_i[k] = i
            f(k + 1, curM + arr[k][i])
            used[i] = False

    return


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result_i = [-1] * N
    used = [False] * N
    resultMin = 1000
    f(0, 0)
    print(f'#{tc}', resultMin)