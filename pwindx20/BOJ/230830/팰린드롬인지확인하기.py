# 10988
# 입력 단어
# 출력: 팰린드롬이면 1, 아니면 0

s = input().strip()
N = len(s)
for i in range(N//2):
    if s[i]!=s[N-1-i]:
        print(0)
        break
else: print(1)