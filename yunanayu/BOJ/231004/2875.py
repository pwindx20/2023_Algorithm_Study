# 대회 or 인턴

N, M, K = map(int, input().split())
ans = 0
while N>=0 and M>=0 and N+M-3>=K:
    N -= 2
    M -= 1
    if N>= 0 and M>=0 and N + M >= K:
        ans += 1
    else:
        break
print(ans)