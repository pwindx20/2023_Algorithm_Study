from sys import stdin
input = stdin.readline

A, B = map(int, input().split())
Arr = list(map(int, input().split()))
Brr = list(map(int, input().split()))
all = set(Arr+Brr)
print(len(all) * 2 - len(Arr) - len(Brr))