number = int(input())
ans = 'int'
for _ in range(number // 4):
    ans = 'long ' + ans
print(ans)