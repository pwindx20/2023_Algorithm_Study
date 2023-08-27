W, H = map(int, input().split())
N = int(input())
arr = [[0]*W for _ in range(H)]
# for r in range(H):
#     print(arr[r])
max_s = 0
w = []
h = []
for _ in range(N):
    d, p = map(int, input().split())
    if d == 0:
        w.append(p)
    else:
        h.append(p)

print(w)
print(h)