N = int(input())
lst = list(map(int, input().split()))
v = int(input())
cnt = 0
for e in lst:
    if e == v:
        cnt += 1
print(cnt)