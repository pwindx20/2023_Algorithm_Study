for test_case in range(1, 5):
    x1, y1, x2, y2 = map(int, input().split())
    arr = [[0] * 50001 for _ in range(50001)]

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            arr[i][j] += 1

cnt = 0
for i in range(x1, x2 + 1):
    for j in range(y1, y2 + 1):
        if arr[i][j] == 2:
            cnt += 1

if cnt == 1:
    print('c')


elif cnt == 0:
    print('d')


elif:
    for i in range(x1, x2+1):
        for j in range(y1, y2 + 1):
            if arr[i][j] == 2 and 0 <= i - 1 < x1 and arr[i - 1][j] == 0 and 0 <= i + 1 < x1 and arr[i + 1][j] == 0:
                print('b')

else:
    print('a')



