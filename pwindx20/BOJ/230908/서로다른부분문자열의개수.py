# 11478
# 입력: 문자열 S
# 출력: 서로 다른 부분 문자열의 개수
import sys
S = sys.stdin.readline()[:-1]
N = len(S)
subset = set()
cnt = 0
for i in range(1,N+1):
    for j in range(0, N+1-i):
        s = S[j:j+i]
        subset.add(s) # list랑 not in을 썼더니 시간초과...
# print(subsetlst)
print(len(subset))