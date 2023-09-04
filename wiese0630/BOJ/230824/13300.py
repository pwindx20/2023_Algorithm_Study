import sys
sys.stdin = open('input13300.txt', 'r')

N, K = map(int, input().split())
arr = [[0]*7 for _ in range(2)]


for test_case in range(1, N+1):
    S, Y = map(int, input().split())
    arr[S][Y] += 1



cnt = 0
for i in range(2):
    for j in range(1,7):
       if arr[i][j] % K == 0:
           cnt += arr[i][j] // K
       else:
           cnt += 1 + (arr[i][j] // K)

print(cnt)

