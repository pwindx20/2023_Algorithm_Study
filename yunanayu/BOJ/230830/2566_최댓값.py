arr = [list(map(int, input().split())) for _ in range(9)]
maxV = 0
i = 0
j = 0
for r in range(9):
    for c in range(9):
        if maxV < arr[r][c]:
            maxV = arr[r][c]
            i = r
            j = c
print(maxV)
print(i+1, j+1)