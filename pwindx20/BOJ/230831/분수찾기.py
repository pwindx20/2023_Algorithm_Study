# 1193
# 입력: X
# 출력: 분수 출력
X = int(input())
i = 2
cnt = 0
isX = False
while not isX:
    for j in range(1,i):
        for k in range(1,i):
            cnt += 1
            if cnt ==X:
                print()
                isX = True
    i += 1