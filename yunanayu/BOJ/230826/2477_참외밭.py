import sys
sys.stdin = open('2477.txt','r')


K = int(input())
arr = [[] for _ in range(5)]
drc = []
W = []
H = []
# print(arr)
for _ in range(6):
    N, L = map(int, input().split())
    drc.append(N)
    arr[N].append(L)
    if N == 3 or N == 4:
        W.append(L)
    else:
        H.append(L)
print(drc)
print(arr)
print(W)
print(H)

S = max(W) * max(H)
print(S)