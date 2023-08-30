# 킹 퀸 룩 비숍 나이트 폰
# 1  1  2   2    2    8
lst = list(map(int, input().split()))
ans = [1, 1, 2, 2, 2, 8]
result = []
for i in range(6):
    result.append(ans[i]-lst[i])
print(*result)