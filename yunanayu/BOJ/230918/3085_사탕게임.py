import sys
sys.stdin = open('input.txt','r')

N = int(input())
arr = [list(input()) for _ in range(N)]
print(arr)
maxV = 0
for r in range(N):
    temp = 0
    cnt = 0
    # for c in range(N):
    while temp < N:
        if arr[r][temp] == arr[r][temp+1]:
            cnt += 1
            temp += 1
        else:
            temp += 1
    if cnt == N:
        print(N)
        break
    else:
