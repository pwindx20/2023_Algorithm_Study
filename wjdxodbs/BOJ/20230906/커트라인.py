from sys import stdin
input = stdin.readline

N, k = map(int, input().split())
arr = list(map(int, input().split()))
lst = [0] * 10001
b = []
for i in arr:
    lst[i] += 1
for i in range(-1, -10002, -1):
    while lst[i]:
        b.append(10001 + i)
        lst[i] -= 1
print(b[k-1])