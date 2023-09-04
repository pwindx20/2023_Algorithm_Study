N, B = input().split()
arr = [str(i) for i in range(10)]
for i in range(65, 91):
    arr.append(chr(i))
n = cnt = 0
for i in range(len(N)-1, -1, -1):
    n += (int(B) ** cnt * arr.index(N[i]))
    cnt += 1
print(n)