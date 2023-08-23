import sys
sys.stdin = open('input2563.txt', 'r')

T = int(input())
blank = [[0]* 100 for _ in range(100)]
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    for i in range(N, N+10):
        for j in range(M, M+10):
            blank[i][j] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if blank[i][j] == 1:
            cnt += 1

print(cnt)