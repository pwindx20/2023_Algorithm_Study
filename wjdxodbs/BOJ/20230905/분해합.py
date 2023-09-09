N = int(input())
l = len(str(N))
for i in range(N-l*9, N):
    sum_n = 0
    if i >= 0:
        for j in str(i):
            sum_n += int(j)
        if i + sum_n == N:
            print(i)
            break
else:
    print(0)