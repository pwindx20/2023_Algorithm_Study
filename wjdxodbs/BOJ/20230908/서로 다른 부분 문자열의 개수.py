S = input()
l = len(S)
cnt = 0
for i in range(len(S)):
    s = set()
    for j in range(l-i):
        s.add(S[j:i+j+1])
    cnt += len(s)
print(cnt)