d1 = {}
d2 = {}
for i in range(3):
    a, b = input().split()
    d1.setdefault(a, 0)
    d2.setdefault(b, 0)
    d1[a] += 1
    d2[b] += 1
for i in d1.keys():
    if d1[i] % 2 == 1:
        print(i, end=' ')
        break
for i in d2.keys():
    if d2[i] % 2 == 1:
        print(i, end=' ')
        break