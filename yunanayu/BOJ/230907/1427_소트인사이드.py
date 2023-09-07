N = list(map(int,input()))
# print(N)
N.sort()
N.reverse()
for n in N:
    print(n,end='')