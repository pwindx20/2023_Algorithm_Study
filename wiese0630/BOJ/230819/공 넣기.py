N, M = map(int, input().split())
lst = [0] * N

for test_case in range(1, M + 1):
    i, j, k = map(int, input().split())
    for num in range(i - 1, j):
        lst[num] = k
for elem in lst:
    print(elem, end=' ')
