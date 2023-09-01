arr = [list(input()) for _ in range(5)]

for i in range(5):
    for j in range(15):
        arr[i][j] == arr[j][i]

print(arr)


#인덱스 아웃 오브 레인지때문에 못하겠습니도
#try except 써봐도 안된다