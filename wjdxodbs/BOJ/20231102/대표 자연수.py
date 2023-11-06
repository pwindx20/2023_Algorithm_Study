from sys import stdin
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
s, e = 0, N
result = 0
min_n = int(1e9)
while s <= e:
    m = (s + e) // 2
    save = sum([abs(i - arr[m]) for i in arr])
    if save <= min_n:
        e = m-1
        min_n = save
        result = arr[m]
    else:
        s = m+1

print(result)