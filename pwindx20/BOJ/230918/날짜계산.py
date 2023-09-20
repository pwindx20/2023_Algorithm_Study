# 1476
#입력: E(1~15), S(1~28), M(1~19)
#출력: 가장 빠른 년도

E, S, M = map(int, input())
e, s, m = 0, 0, 0
if S == M:
    print(S)
else:
    while True:
        if e*15+E != s*28+S:
            e+1
            
        for m in range(e):
            for s in range(m):
