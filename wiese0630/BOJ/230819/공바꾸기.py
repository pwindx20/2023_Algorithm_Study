N, M = map(int, input().split())
lst = []
for e in range(1, N + 1):
    lst += [e]

for change in range(1, M + 1):
    i, j = map(int, input().split())
    lst[i - 1], lst[j-1] = lst[j-1], lst[i - 1]

for elem in lst:
    print(elem, end=' ')