from sys import stdin
input = stdin.readline

N = int(input())
st = [[] for _ in range(51)]
for i in range(N):
    a = input().rstrip()
    l = len(a)
    st[l].append(a)
for i in range(51):
    if st[i]:
        st[i] = sorted(set(st[i]))
for i in st:
    if i:
        print(*i, sep='\n')