def side(N):
    if N == 1:
        return 3
    else:
        return 2*side(N-1) - 1

N = int(input())

print(side(N)**2)