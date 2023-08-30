# 2941
s= input().strip()
alph = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
for a in alph:
    cnt += s.count(a)
    if a=='z=':
        cnt -=s.count('dz=')
print(len(s)-cnt-s.count('dz='))