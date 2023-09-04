while True:
    N = int(input())
    result = []
    if N == -1:
        break
    for i in range(1,N):
        if N % i == 0:
            result.append(i)
    result.sort()
    if N == sum(result):
        print(f'{N} =', end=' ')
        print(*result, sep=' + ')
    else:
        print(f'{N} is NOT perfect.')
