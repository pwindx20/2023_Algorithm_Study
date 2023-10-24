def a(n):
    global cnt
    if n == N:
        cnt += 1
        return

    for i in range(1, 4):
        if n + i <= N:
            a(n+i)
        else:
            break


for _ in range(int(input())):
    N = int(input())
    cnt = 0
    for i in range(1, 4):
        a(i)
    print(cnt)