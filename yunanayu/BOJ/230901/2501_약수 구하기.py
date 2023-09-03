result = []
N, K = map(int, input().split())
for n in range(1, N+1):
    if N % n == 0:
        result.append(n)
result.sort()
if len(result) < K:
    print(0)
else:
    print(result[K-1])