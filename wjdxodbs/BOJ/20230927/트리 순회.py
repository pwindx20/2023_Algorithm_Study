import sys
input = sys.stdin.readline

def prefix(n):
    if n in v:
        print(k[v.index(n)], end='')
        if 2 * n in v:
            prefix(2 * n)
        if 2 * n + 1 in v:
            prefix(2 * n + 1)


def infix(n):
    if n in v:
        if 2 * n in v:
            infix(2 * n)
        print(k[v.index(n)], end='')
        if 2 * n + 1 in v:
            infix(2 * n + 1)


def postfix(n):
    if n in v:
        if 2 * n in v:
            postfix(2 * n)
        if 2 * n + 1 in v:
            postfix(2 * n + 1)
        print(k[v.index(n)], end='')


N = int(input())
d = {}
idx = 1
for i in range(N):
    a, b, c = input().split()
    if not d.get(a, 0):
        d[a] = idx
    else:
        idx = d[a]
    if b != '.':
        d[b] = 2 * idx
    if c != '.':
        d[c] = 2 * idx + 1
k = list(d.keys())
v = list(d.values())
prefix(1)
print()
infix(1)
print()
postfix(1)
