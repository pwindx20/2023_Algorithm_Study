T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(N, M, arr)

    maxV = 0
    for i in range(N):
        for j in range(N):
            sumV = arr[i][j]
            sumVV = arr[i][j]
            for k in range(1, M):
                for di, dj in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
                    ni = i + k * di
                    nj = j + k * dj
                    if 0 <= ni < N and 0 <= nj < N:
                        sumV += arr[ni][nj]
                for ddi, ddj in [[1, -1], [1, 1], [-1, -1], [-1, 1]]:
                    nni = i + k * ddi
                    nnj = j + k * ddj
                    if 0 <= nni < N and 0 <= nnj < N:
                        sumVV += arr[nni][nnj]
            if sumV > maxV:
                maxV = sumV
            if sumVV > maxV:
                maxV = sumVV
    print(f'#{test_case} {maxV}')