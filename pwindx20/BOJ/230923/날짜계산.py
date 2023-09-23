# 1476
# 입력: E(15), S(28), M(19)
# 출력: 가장 빠른 연도

E, S, M = map(int,input().split())
i = 1
while i%15 !=E%15 or i%28 != S%28 or i%19 !=M%19:
    i+=1
print(i)