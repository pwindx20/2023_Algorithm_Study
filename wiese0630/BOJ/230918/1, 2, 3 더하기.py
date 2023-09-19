def plus(N):
    if N >= 4:
        return plus(N-1) + plus(N-2) + plus(N-3)

    elif N == 3:
        return plus(2) + plus(1) + 1
    
    elif N == 2:
        return plus(1) + 1
    
    else:
        return 1



T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    print(plus(N))