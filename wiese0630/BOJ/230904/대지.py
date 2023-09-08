N = int(input())

lst_w = []
lst_h = []
for test_case in range(1, N+1):
    W, H = map(int, input().split())
    lst_w.append(W)
    lst_h.append(H)

height = max(lst_h) - min(lst_h)
width = max(lst_w) - min(lst_w)

print(width * height)
