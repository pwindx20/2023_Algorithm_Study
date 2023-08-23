
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    cntarr = [0]*201
    # print(cntarr)

    for X, Y in arr:
        if X > Y:
            X, Y = Y, X
        # print(X, Y)
        for i in range((X+1)//2, (Y+1)//2 + 1):
            cntarr[i] += 1
    # print(cntarr)

    maxV = 0
    for x in cntarr:
        if x > maxV:
            maxV = x

    print(f'#{test_case} {maxV}')
