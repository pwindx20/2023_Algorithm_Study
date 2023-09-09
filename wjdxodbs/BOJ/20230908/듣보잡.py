from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
d = {input().rstrip(): 1 for _ in range(N)}
arr2 = [input().rstrip() for _ in range(M)]
st = []
for i in arr2:
    if d.get(i, 0):
        st.append(i)
print(len(st))
print(*sorted(st), sep='\n')