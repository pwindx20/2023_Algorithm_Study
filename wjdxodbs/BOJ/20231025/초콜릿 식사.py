K = int(input())
n = 1
cnt = 0
while n < K:
    n = n << 1

print(n, end=' ')

while K > 0:
    if K >= n:
        K -= n
    else:
        n //= 2
        cnt += 1

print(cnt)