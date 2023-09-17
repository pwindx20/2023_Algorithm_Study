X = int(input())
N = int(input())

sumV = 0
for test_case in range(1, N+1):
    p, n = map(int, input().split())
    sumV += p*n
if sumV = X:
    print('Yes')
else:
    print('No')