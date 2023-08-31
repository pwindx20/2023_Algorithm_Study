# 3003
pieces = [1, 1, 2, 2, 2, 8]
pieces_h = list(map(int, input().split()))
for i in range(6):
    print(pieces[i]-pieces_h[i], end=' ')