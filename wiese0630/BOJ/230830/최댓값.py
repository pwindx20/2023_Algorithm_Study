arr = [list(map(int, input().split())) for _ in range(9)]

maxV = -1
maxi = -1
maxj = -1
for i in range(9):
    for j in range(9):
        if arr[i][j] > maxV:
            maxV = arr[i][j]
            maxi = i
            maxj = j
print(maxV)
print(maxi+1, maxj+1)