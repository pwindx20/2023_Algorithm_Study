import sys
sys.stdin = open('input10163.txt', 'r')

paper = [[0]* 1001 for _ in range(1001)]
T = int(input())

for n in range(1, T+1):
    cnt = 0
    r, c, M, N = map(int, input().split())
    # print(r, c, M, N)
    for i in range(r, r+M):
        for j in range(c, c+N):
            paper[i][j] = n

for n in range(1, T+1):
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if paper[i][j] == n:
                cnt += 1
    print(cnt)