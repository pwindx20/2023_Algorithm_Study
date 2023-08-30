# 2566
arr = [list(map(int,input().split())) for _ in range(9)]
max_num = -1 # 0으로 했다가 틀림
index = (0,0)
for i in range(9):
    for j in range(9):
        if max_num<arr[i][j]:
            index = (i+1, j+1)
            max_num = arr[i][j]
print(max_num)
print(*index)