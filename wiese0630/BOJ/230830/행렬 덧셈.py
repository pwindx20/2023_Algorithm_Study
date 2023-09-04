N, M = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(N)]
arr2 = [list(map(int, input().split())) for _ in range(N)]
arr3 = [[0]*M for _ in range(N)]
#N, M 틀려서 인덱스 에러가 났다 조심하자!

for i in range(N):
    for j in range(M):
        arr3[i][j] = arr1[i][j] + arr2[i][j]

for row in arr3:
    for elem in row:
        print(elem, end=' ')
    print()