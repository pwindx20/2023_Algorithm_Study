result = []
N, K = map(int, input().split())
for n in range(1, N+1):
    result.append(N%n)
result.sort()
print(result[K-1])