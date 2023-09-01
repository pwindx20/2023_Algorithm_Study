X = int(input())
N = int(input())
sum_V = 0
for _ in range(N):
    a , b = map(int, input().split())
    sum_V += a * b
if sum_V == X:
    print('Yes')
else:
    print('No')