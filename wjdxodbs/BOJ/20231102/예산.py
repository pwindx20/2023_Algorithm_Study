from sys import stdin
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())
result = 0
s, e = 0, arr[-1]
while s <= e:
    m = (s+e) // 2
    save = 0
    for i in arr:
        if m < i:
            save += m
        else:
            save += i
    if save <= M:
        result = m
        s = m+1
    else:
        e = m-1

print(result)