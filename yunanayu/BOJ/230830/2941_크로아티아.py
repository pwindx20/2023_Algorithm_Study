lst = ['c=','c-','dz=','d-','lj','nj','s=','z=']
S = input()
cnt = 0
for l in lst:
    if l in S:
        cnt += 1
print(cnt)