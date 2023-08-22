N, M = map(int, input().split())
T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]
X, Y = map(int, input().split())
ans1 = 0
ans2 = 0
ans3 = 0
ans4 = 0
for D1, D2 in arr:
    if D1 == 1:
        ans1 = min(X+M+D2, (N-X)+M+(N-D2))
    elif D1 == 2:
        ans2 = abs(D2 - X)
    elif D1 == 3:
        ans3 = X+(M-D2)
    else:
        ans4 = ((N-X)+(M+D2-2))
ans = ans1 + ans2 + ans3 + ans4
print(ans)