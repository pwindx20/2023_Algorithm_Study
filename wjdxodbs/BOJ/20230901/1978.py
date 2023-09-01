N = int(input())
cnt = 0
for i in map(int, input().split()):
    c = 0
    for j in range(1, i+1):
        if not i % j:
            c += 1
        if c > 2:
            break
    if c == 2:
        cnt += 1
print(cnt)