arr = sorted(list(map(int, input())), reverse=True)

if arr[-1] != 0:
    print(-1)
else:
    sum_n = 0
    for i in arr:
        sum_n += i

    if sum_n % 3:
        print(-1)
    else:
        print(*arr, sep='')