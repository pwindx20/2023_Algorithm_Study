# 1316
N = int(input())
cnt = 0
for _ in range(N):
    s = input().strip()
    for i in range(len(s)-1):
        if s[i]!= s[i+1] and s[i+1:].count(s[i])>0:
            break
    else: cnt += 1
print(cnt)