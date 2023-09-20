T = int(input())

for test_case in range(1, T+1):
    M, N, x, y = map(int, input().split())

    # print(M, N, x, y)

    for i in range(N):
        for j in range(M):
            if i*M + x == j*N + y:
                print(i*M + x)
                break
            break
        break


    #중국인의 나머지 정리 어떻게 하는지 모르겠어요
