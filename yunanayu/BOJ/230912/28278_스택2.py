import sys

N = int(sys.stdin.readline())
ST = []
for _ in range(N):
    n = list(map(int, sys.stdin.readline().split()))
    if n[0] == 1:
        ST.append(n[1])
    elif n[0] == 2:
        if ST:
            print(ST.pop())
        else:
            print(-1)
    elif n[0] == 3:
        print(len(ST))
    elif n[0] == 4:
        if ST:
            print(0)
        else:
            print(1)
    else:
        if ST:
            print(ST[-1])
        else:
            print(-1)

