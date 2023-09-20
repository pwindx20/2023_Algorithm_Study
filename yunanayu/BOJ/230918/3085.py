# 사탕 게임

N = int(input())
arr = [list(input()) for _ in range(N)]
# print(arr)
r = 0
c = 0
while c < N:
    if arr[r][c] != arr[r][c+1]:

